from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
import sqlite3

# подключение к sqlite БД для событий
def sqlite_connection() -> async_sessionmaker[AsyncSession] | None:
    
    url = "sqlite+aiosqlite:///backend/sqlite.db"

    try:
        engine = create_async_engine(url, connect_args={"check_same_thread": False})
        return async_sessionmaker(autocommit=False, autoflush=False, bind=engine)
    except sqlite3.DatabaseError:
        return None 
