from persistent.db.base import Base, WithId
from sqlalchemy import Column, Text, DateTime

# таблица мероприятий
class Event(Base, WithId):
    __tablename__ = "event"

    event_name = Column(Text, nullable=False)
    event_datetime = Column(DateTime, nullable=False)
    event_content = Column(Text)
    event_tags = Column(Text)
