import multiprocessing as mp

from loguru import logger
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from config.config import PG_USER, PG_HOST, PG_PORT, PG_PASSWORD, DB


class Postgres(BaseModel):
    database: str = DB
    host: str = PG_HOST
    port: int = PG_PORT
    username: str = PG_USER
    password: str = PG_PASSWORD
    

class Uvicorn(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    workers: int = mp.cpu_count()*2 + 1
    

class _Settings(BaseSettings):
    pg: Postgres = Postgres()
    uvicorn: Uvicorn = Uvicorn()
    
    model_config = SettingsConfigDict(env_file=".env", env_prefix="app_", env_nested_delimiter="__")
    
    
settings = _Settings()
logger.info("settings.inited {}", settings.model_dump_json())
 