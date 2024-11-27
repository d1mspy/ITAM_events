from persistent.db.base import Base, WithId
from sqlalchemy import Column, Text, DateTime

# таблица мероприятий
class Event(Base, WithId):
    __tablename__ = "event"

    name = Column(Text, nullable=False)
    start_datetime = Column(DateTime, nullable=False)
    end_datetime = Column(DateTime,  nullable=False)
    place = Column(Text, nullable=False)
    content = Column(Text)
    category = Column(Text)
    tags = Column(Text)
