from persistent.db.base import Base, WithId, With_created_at, With_updated_at
from sqlalchemy import Column, Text, DateTime, BigInteger, Date

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
    
# таблица пользователей
class User(Base, With_created_at, With_updated_at):
    __tablename__ = "user_data"
    
    id = Column(Text, primary_key=True)
    email = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    surname = Column(Text, nullable=False)
    age = Column(BigInteger, nullable=False)
    user_group = Column(Text)

# таблица пользователей, зарегестрированных на мероприятия 
class RegisteredUsers(Base, WithId, With_created_at, With_updated_at):
    __tablename__ = "registered_users" 

    user_id = Column(Text, nullable=False)
    event_id = Column(Text, nullable=False)
