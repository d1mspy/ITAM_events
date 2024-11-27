from fastapi import FastAPI, Path, status, HTTPException
from repositories.db.event_repository import EventRepository
from datetime import datetime

app = FastAPI(
    title="ITAM мероприятия",
    description="микросервис для управления мероприятиями на платформе ITAM"
)

event = EventRepository()


@app.post("/events")
async def post_event(name: str,
                     start_year: int, start_month: int, start_day: int, start_hour: int, start_minute: int, 
                     end_year: int, end_month: int, end_day: int, end_hour: int, end_minute: int, 
                     place: str, content: str, category: str, tags: str) -> None:
    """
    создание мероприятия
    """

    start_datetime = datetime(start_year, start_month, start_day, start_hour, start_minute)
    end_datetime = datetime(end_year, end_month, end_day, end_hour, end_minute)
    
    await event.post_event(name, start_datetime, end_datetime, place, content, category, tags)


@app.get("/events/{event_id}")
async def get_event(event_id: str = Path(...)) -> dict | None:
    """
    получение информации о мероприятии по id
    """
    info = await event.get_event(event_id)
    if info is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="мероприятие не найдено")

    return info


@app.put("/events/{id}")
async def put_event(name: str,
                    start_year: int, start_month: int, start_day: int, start_hour: int, start_minute: int, 
                    end_year: int, end_month: int, end_day: int, end_hour: int, end_minute: int, 
                    place: str, content: str, category: str, tags: str, id: str = Path(...)) -> None:
    """
    обновление информации о мероприятии
    """

    start_datetime = datetime(start_year, start_month, start_day, start_hour, start_minute)
    end_datetime = datetime(end_year, end_month, end_day, end_hour, end_minute)

    await event.put_event(id, name, start_datetime, end_datetime, place, content, category, tags)


@app.delete("/events/{event_id}")
async def delete_event(event_id: str = Path(...)) -> None:
    """
    Удаление мероприятия
    """
    await event.delete_event(event_id)


@app.get("/events")
async def get_all_events() -> list | None:
    """
    Получение информации о всех мероприятиях
    """
    info = await event.get_all_events()

    return info
