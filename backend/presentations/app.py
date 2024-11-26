from fastapi import FastAPI, Path
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
async def get_event(event_id: str = Path(...)) -> dict:
    """
    получение информации о мероприятии по id
    """
    info = await event.get_event(event_id)

    return info

@app.put("/events/{event_id}")
async def put_event() -> None:
    ...
