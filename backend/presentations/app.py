from fastapi import FastAPI
from repositories.db.event_repository import EventRepository
from datetime import datetime

app = FastAPI(
    title="ITAM мероприятия",
    description="микросервис для управления мероприятиями на платформе ITAM"
)

@app.get("/test")
def test() -> str:
    return "itam"


@app.post("/events")
async def post_event(name: str, year: int, month: int, day: int, hour: int, minute: int, content: str, tags: str) -> None:
    """
    создание мероприятия
    """

    event_datetime = datetime(year, month, day, hour, minute)
    
    event = EventRepository()
    await event.post_event(name, event_datetime, content, tags)
