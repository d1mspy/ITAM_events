from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Text
import uuid

Base = declarative_base()

# возваращает uuid в строковом виде
def _uuid4_to_str() -> str:
    return str(uuid.uuid4())

# класс для добавления столбца id в таблицу
class WithId:
    __abstract__ = True

    id = Column(Text, default=_uuid4_to_str, primary_key=True)


class WithRegisterId:
    __abstract__ = True

    register_id = Column(Text, default=_uuid4_to_str, primary_key=True)
