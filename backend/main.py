from presentations.app import app
from repositories.db.event_repository import EventRepository
import uvicorn

# запуск 
uvicorn.run(app)
