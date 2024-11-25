from persistent.db.event import Event
from infrastructure.db.connect import sqlite_connection
from sqlalchemy import insert
from datetime import datetime

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
