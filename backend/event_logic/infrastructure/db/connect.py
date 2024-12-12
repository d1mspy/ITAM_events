from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from config.config import DB_URL

# подключение к sqlite БД для событий
def sqlite_connection() -> async_sessionmaker[AsyncSession] | None:
    
    engine = create_async_engine(DB_URL, connect_args={"check_same_thread": False})
    return async_sessionmaker(autocommit=False, autoflush=False, bind=engine)
