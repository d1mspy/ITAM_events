from fastapi import FastAPI, Path, status, HTTPException, Security
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader
from services.JWTservice import check_access_token
from repositories.db.event_repository import EventRepository
from sqlalchemy.exc import OperationalError, ArgumentError
from datetime import datetime
from pydantic import BaseModel
from services.JWTservice import check_access_token


app = FastAPI(
    title="ITAM мероприятия",
    description="микросервис для управления мероприятиями на платформе ITAM"
)


# экземпляр класса для взаимодействия с базой данных
event_rep = EventRepository()

class UserInfo(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    age: int
    group: str

# класс мероприятия
class Event(BaseModel):
    name: str
    start_year: int
    start_month: int
    start_day: int
    start_hour: int
    start_minute: int
    end_year: int
    end_month: int
    end_day: int
    end_hour: int
    end_minute: int
    place: str
    content: str
    category: str
    tags: str
    max_people: int


# разрешение запросов из сторонних сервисов(для фронтенда)
def allow_requests() -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )


@app.post("/")
async def post_event(event: Event, authorization_header: str = Security(APIKeyHeader(name='Authorization', auto_error=False))) -> None:
    """
    создание мероприятия
    """
    user_data = await check_access_token(authorization_header)
    
    if not user_data['is_admin']:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="создавать мероприятия может только администратор")


    start_datetime = datetime(event.start_year, event.start_month, event.start_day, event.start_hour, event.start_minute)
    end_datetime = datetime(event.end_year, event.end_month, event.end_day, event.end_hour, event.end_minute)
    
    try:
        await event_rep.post_event(event.name, start_datetime, end_datetime, event.place, event.content, event.category, event.tags)
    except OperationalError:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Отсутствует база данных или соответствующее поле")


@app.get("/{id}")
async def get_event(id: str = Path(...)) -> dict | None:
    """
    получение информации о мероприятии по id
    """
    
    try:
        info = await event_rep.get_event(id)
    except OperationalError:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Отсутствует база данных или соответствующее поле")

    if info is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Мероприятие не найдено")

    return info


@app.put("/{id}")
async def put_event(event: Event, id: str = Path(...), authorization_header: str = Security(APIKeyHeader(name='Authorization', auto_error=False))) -> None:
    """
    обновление информации о мероприятии
    """
    user_data = await check_access_token(authorization_header)
    
    if not user_data['is_admin']:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="обновлять мероприятия может только администратор")


    start_datetime = datetime(event.start_year, event.start_month, event.start_day, event.start_hour, event.start_minute)
    end_datetime = datetime(event.end_year, event.end_month, event.end_day, event.end_hour, event.end_minute)

    try:
        await event_rep.put_event(id, event.name, start_datetime, end_datetime, event.place, event.content, event.category, event.tags)
    except OperationalError:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Отсутствует база данных или соответствующее поле")
    except ArgumentError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Мероприятие не найдено")


@app.delete("/events/{id}")
async def delete_event(id: str = Path(...), authorization_header: str = Security(APIKeyHeader(name='Authorization', auto_error=False))) -> None:
    """
    Удаление мероприятия
    """
    user_data = await check_access_token(authorization_header)
    
    if not user_data['is_admin']:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="удалять мероприятия может только администратор")
    
    try:
        await event_rep.delete_event(id)
    except OperationalError:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Отсутствует база данных или соответствующее поле")
    except ArgumentError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Мероприятие не найдено")


@app.get("/")
async def get_all_events() -> list:
    """
    получение информации о всех мероприятиях
    """
    try:
        info = await event_rep.get_all_events()
    except OperationalError:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Отсутствует база данных или соответствующее поле")
    return info


@app.post("/{id}")
async def register_on_event(id: str = Path(...), authorization_header: str = Security(APIKeyHeader(name='Authorization', auto_error=False))) -> dict:
    """
    регистрация на мероприятие
    """
    user_data = await check_access_token(authorization_header)
    
    if not event_rep.check_registration(id, user_data['id']):
        return {"detail": "already registered"}
    
    detail = await event_rep.register_on_event(id, user_data['id'])
    return detail


@app.delete("/registrations/{id}")
async def cancel_registration(id: str = Path(...), authorization_header: str = Security(APIKeyHeader(name='Authorization', auto_error=False))) -> dict:
    """
    отмена регистрации на мероприятие
    """
    user_data = await check_access_token(authorization_header)

    if event_rep.check_registration(id, user_data['id']):
        detail = await event_rep.cancel_registration(id, user_data['id'])
        return detail
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='пользователь не зарегистрирован на мероприятие')
    

@app.post("/user_data")
async def save_user(user: UserInfo) -> None:
    """
    эндпоинт для получение информации о зарегистрировавшемся пользователе
    """
    detail = await event_rep.save_user(user.id, user.email, user.first_name, user.last_name, user.age, user.group)
    if detail is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)