from persistent.db.tables import Event, User, RegisteredUsers
from infrastructure.db.connect import sqlite_connection
from sqlalchemy import insert, select, update, delete
from services.mail_service import send_message 
from sqlalchemy.exc import ArgumentError 
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
            search_id = select(Event).where(Event.id == id) 
            id_found = len(list(await session.execute(search_id)))
            if id_found:
                await session.execute(stmp)
                await session.commit()
            else:
                raise ArgumentError

    # удаление мероприятия
    async def delete_event(self, id: str) -> None:
        """
        DELETE FROM event WHERE id = {event_id}
        """
        stmp = delete(Event).where(Event.id == id)

        async with self._sessionmaker() as session:
            search_id = select(Event).where(Event.id == id) 
            id_found = len(list(await session.execute(search_id)))
            if id_found:
                await session.execute(stmp)
                await session.commit()
            else:
                raise ArgumentError

    # получение информации о всех мероприятиях
    async def get_all_events(self) -> list | None:
        """
        SELECT * FROM event
        """
        stmp = select(Event.id, Event.name, Event.start_datetime, Event.end_datetime, Event.place, Event.content, Event.category, Event.tags)

        async with self._sessionmaker() as session:
            resp = await session.execute(stmp)
            await session.commit()
        
        row = list(resp.fetchall())
        if len(row) == 0:
            return None
        
        keys = ["id", "name", "start_datetime", "end_datetime", "place", "content", "category", "tags"]
        info = [dict(zip(keys, item)) for item in row]

        return info
        
    # регистрация на мероприятие
    async def register_on_event(self, event_id: str, user_id: str) -> dict:
        
        stmp = insert(RegisteredUsers).values({"user_id": user_id, "event_id": event_id})
        
        async with self._sessionmaker() as session:
            await session.execute(stmp)
            await session.commit()
            
        return {"detail": "successfully registered"}
    
    # отмена регистрации на мероприятие
    async def cancel_registration(self, event_id: str, user_id: str) -> dict:
        
        stmp = delete(RegisteredUsers).where(RegisteredUsers.event_id == event_id and RegisteredUsers.user_id == user_id)
        
        async with self._sessionmaker() as session:
            await session.execute(stmp)
            await session.commit()
        
        return {"detail": "successfully cancelled registration"}
    
    # проверка регистрации пользователя на мероприятие
    async def check_registration(self, event_id: str, user_id: str) -> bool:
        
        stmp = select(RegisteredUsers.id).where(RegisteredUsers.user_id == user_id and RegisteredUsers.event_id == event_id)
        
        async with self._sessionmaker as session:
            resp = await session.execute(stmp)
            
        row = resp.fetchall()
        
        if row is None:
            return False
        return True
    
    #сохранение информации о пользователе в бд
    async def save_user(self, id, email, first_name, last_name, age, group) -> None | str:
        
        stmp = select(User).where(User.id == id)
        
        async with self._sessionmaker as session:
            resp = await session.execute(stmp)
            
        row = resp.fetchall()
        
        if row is not None:
            return "User already exists"
        
        stmp = insert(User).values({"id": id, "email": email, "name": first_name, "surname": last_name, "age": age, "group": group})
        
        async with self._sessionmaker as session:
            await session.execute(stmp)
            await session.commit()
        