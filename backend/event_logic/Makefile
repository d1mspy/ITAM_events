docker-build:
	docker build -t="app" .

docker-rerun:
	docker rm app || true
	docker run --name=app -p 8000:8000 -e APP_UVICORN='{"host": "0.0.0.0"}' app

