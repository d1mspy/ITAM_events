from presentations.app import app
from repositories.db.event_repository import EventRepository
import uvicorn

# запуск 
def main() -> None:
    uvicorn.run(app)


if __name__ == "__main__":
    main()
