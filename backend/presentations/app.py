from typing import List
from fastapi.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from fastapi import FastAPI, Path, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from repositories.db.event_repository import EventRepository
from sqlalchemy.exc import OperationalError, ArgumentError
from datetime import datetime
from pydantic import BaseModel, EmailStr


app = FastAPI(
    title="ITAM мероприятия",
    description="микросервис для управления мероприятиями на платформе ITAM"
)


# экземпляр класса для взаимодействия с базой данных
event_rep = EventRepository()


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
async def post_event(event: Event) -> None:
    """
    создание мероприятия
    """

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
async def put_event(event: Event, id: str = Path(...)) -> None:
    """
    обновление информации о мероприятии
    """

    start_datetime = datetime(event.start_year, event.start_month, event.start_day, event.start_hour, event.start_minute)
    end_datetime = datetime(event.end_year, event.end_month, event.end_day, event.end_hour, event.end_minute)

    try:
        await event_rep.put_event(id, event.name, start_datetime, end_datetime, event.place, event.content, event.category, event.tags)
    except OperationalError:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Отсутствует база данных или соответствующее поле")
    except ArgumentError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Мероприятие не найдено")


@app.delete("/{id}")
async def delete_event(id: str = Path(...)) -> None:
    """
    Удаление мероприятия
    """
    try:
        await event_rep.delete_event(id)
    except OperationalError:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Отсутствует база данных или соответствующее поле")
    except ArgumentError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Мероприятие не найдено")


@app.post("/{id}")
async def register_on_event(id: str = Path(...)) -> None:
    ...


@app.delete("/{id}")
async def cancel_registration(id: str = Path(...)) -> None:
    ...
