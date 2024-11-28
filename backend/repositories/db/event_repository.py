from persistent.db.event import Event
from infrastructure.db.connect import sqlite_connection
from sqlalchemy import insert, select, update, delete
from datetime import datetime

# класс для взаимодействия с бд мероприятий
class EventRepository:

    # подключение к sqlite
    def __init__(self):
        self._sessionmaker = sqlite_connection()

    # создание мероприятия
    async def post_event(self, name: str, start_datetime: datetime, end_datetime: datetime, 
                         place: str, content: str, category: str, tags: str) -> None:
        """
        INSERT INTO event(name, start_datetime, end_datetime, place, content, category, tags)
        VALUES ({name}, {start_datetime}, {end_datetime}, {place}, {content}, {category}, {tags})
        """

        stmp = insert(Event).values({"name": name, "start_datetime": start_datetime, "end_datetime": end_datetime, 
                                     "place": place, "content": content, "category": category, "tags": tags})

        async with self._sessionmaker() as session:
            await session.execute(stmp)
            await session.commit()

    # получение информации о мероприятии по id
    async def get_event(self, event_id: str) -> dict | None:
        """
        SELECT * FROM event WHERE id = {event_id}
        """
        stmp = select(Event.id, Event.name, Event.start_datetime, Event.end_datetime, Event.place, 
                      Event.content, Event.category, Event.tags).where(Event.id == event_id)

        async with self._sessionmaker() as session:
            resp = await session.execute(stmp)

        try:
            row = list(resp.fetchone())
        except Exception:
            return None

        keys = ["id", "name", "start_datetime", "end_datetime", "place", "content", "category", "tags"]
        info = dict(zip(keys, row))

        return info
    
    # обновление информации о мероприятии 
    async def put_event(self, id: str, name: str, start_datetime: datetime, end_datetime: datetime, 
                        place: str, content: str, category: str, tags: str) -> None:
        """
        UPDATE event SET 
        name = {name}, start_datetime = {start_datetime}, end_datetime = {end_datetime}, 
        place = {place}, content = {content}, category = {category}, tags = {tags} 
        WHERE id = {event_id}
        """
        stmp = update(Event).values({"name": name, "start_datetime": start_datetime, "end_datetime": end_datetime, 
                                    "place": place, "content": content, "category": category, "tags": tags}).where(Event.id == id)

        async with self._sessionmaker() as session:
            await session.execute(stmp)
            await session.commit()

    # удаление мероприятия
    async def delete_event(self, id: str) -> None:
        """
        DELETE FROM event WHERE id = {event_id}
        """
        stmp = delete(Event).where(Event.id == id)

        async with self._sessionmaker() as session:
            await session.execute(stmp)
            await session.commit()

    # получение информации о всех мероприятиях
    async def get_all_events(self) -> list | None:
        """
        SELECT * FROM event
        """
        stmp = select(Event.id, Event.name, Event.start_datetime, Event.end_datetime,
                      Event.place, Event.content, Event.category, Event.tags)

        async with self._sessionmaker() as session:
            resp = await session.execute(stmp)
            await session.commit()
        
        try:
            row = list(resp.fetchall())
        except Exception:
            return None
        
        keys = ["id", "name", "start_datetime", "end_datetime", "place", "content", "category", "tags"]
        info = [dict(zip(keys, item)) for item in row]

        return info
        
