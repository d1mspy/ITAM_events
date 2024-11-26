from persistent.db.event import Event
from infrastructure.db.connect import sqlite_connection
from sqlalchemy import insert, select
from datetime import datetime

# класс для взаимодействия с бд мероприятий
class EventRepository:

    def __init__(self):
        self._sessionmaker = sqlite_connection()


    async def post_event(self, name: str, event_datetime: datetime, content: str, tags: str) -> None:
        """
        INSERT INTO event(event_name, event_datetime, event_content, event_tags) VALUES ({name}, {datetime}, {content}, {tags})
        """

        stmp = insert(Event).values({"event_name": name, "event_datetime": event_datetime, "event_content": content, "event_tags": tags})

        async with self._sessionmaker() as session:
            await session.execute(stmp)
            await session.commit()


    async def get_event(self, event_id: str) -> dict:
        """
        SELECT * FROM event WHERE id = {event_id}
        """
        stmp = select(Event.id, Event.event_name, Event.event_datetime, Event.event_content, Event.event_tags).where(Event.id == event_id)

        async with self._sessionmaker() as session:
            resp = await session.execute(stmp)

        row = list(resp.fetchone())
        keys = ["id", "event_name", "event_datetime", "event_content", "event_tags"]

        if row is None:
            return None
    
        info = dict(zip(keys, row))

        return info