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


class RegistredUsers(Base):
    __tablename__ = "registred_users" 

    name = Column(Text, nullable=False) 
    email = Column(Text, nullable=False)
    group = Column(Text, nullable=False) 
    event_id = Column(Text, nullable=False)
