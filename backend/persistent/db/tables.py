from persistent.db.base import Base, WithId, With_created_at, With_updated_at
from sqlalchemy import Column, Text, DateTime, BigInteger

# таблица мероприятий
class Event(Base, WithId, With_created_at, With_updated_at):
    __tablename__ = "event"

    name = Column(Text, nullable=False)
    start_datetime = Column(DateTime, nullable=False)
    end_datetime = Column(DateTime,  nullable=False)
    place = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    category = Column(Text)
    tags = Column(Text)
    max_people = Column(BigInteger)

# таблица пользователей, зарегестрированных на мероприятия 
class RegistredUsers(Base, WithId, With_created_at, With_updated_at):
    __tablename__ = "registered_users" 

    event_id = Column(Text, nullable=False)
