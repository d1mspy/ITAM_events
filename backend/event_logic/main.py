from presentations.app import app, allow_requests
import uvicorn

# запуск 
def main() -> None:
    allow_requests()
    uvicorn.run(app)


if __name__ == "__main__":
    main()
