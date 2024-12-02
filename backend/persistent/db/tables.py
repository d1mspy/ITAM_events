from persistent.db.base import Base, WithId
from sqlalchemy import Column, Text, DateTime

# таблица мероприятий
class Event(Base, WithId):
    __tablename__ = "event"

    name = Column(Text, nullable=False)
    start_datetime = Column(DateTime, nullable=False)
    end_datetime = Column(DateTime,  nullable=False)
    place = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    category = Column(Text)
    tags = Column(Text)

# таблица пользователей, зарегестрированных на мероприятия 
class RegistredUsers(Base, WithId):
    __tablename__ = "registred_users" 

    event_id = Column(Text, nullable=False)
