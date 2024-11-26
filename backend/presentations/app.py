from fastapi import FastAPI, Path, status, HTTPException
from repositories.db.event_repository import EventRepository
from datetime import datetime

app = FastAPI(
    title="ITAM мероприятия",
    description="микросервис для управления мероприятиями на платформе ITAM"
)


@app.get("/test")
def test() -> str:
    return "itam"


event = EventRepository()


@app.post("/events")
async def post_event(name: str, year: int, month: int, day: int, hour: int, minute: int, content: str, tags: str) -> None:
    """
    создание мероприятия
    """

    event_datetime = datetime(year, month, day, hour, minute)
    
    await event.post_event(name, event_datetime, content, tags)


@app.get("/events/{event_id}")
async def get_event(event_id: str = Path(...)) -> dict | None:
    """
    получение информации о мероприятии по id
    """
    info = await event.get_event(event_id)
    if info is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="мероприятие не найдено")

    return info


@app.put("/events/{event_id}")
async def put_event(name: str, year: int, month: int, day: int, hour: int, minute: int, content: str, tags: str, event_id: str = Path(...)) -> None:
    """
    обновление информации о мероприятии
    """

    event_datetime = datetime(year, month, day, hour, minute)

    await event.put_event(event_id, name, event_datetime, content, tags)


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
