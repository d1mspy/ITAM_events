from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Text, DateTime
from datetime import datetime
import uuid

Base = declarative_base()

# возваращает uuid в строковом виде
def _uuid4_to_str() -> str:
    return str(uuid.uuid4())

# класс для добавления столбца id в таблицу
class WithId:
    __abstract__ = True

    id = Column(Text, default=_uuid4_to_str, primary_key=True)


class With_created_at():
    __abstract__ = True
    
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    
    
class With_updated_at():
    __abstract__ = True
    
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
