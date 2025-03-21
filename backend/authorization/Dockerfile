FROM golang:1.23.1-alpine

RUN apk update
RUN apk upgrade --no-cache
RUN apk add --no-cache git

WORKDIR /app

COPY go.mod go.sum ./
RUN apk add --no-cache build-base
RUN go mod download
COPY . .
RUN CGO_ENABLED=1 go build -o main ./cmd/auth_service/main.go

EXPOSE 8080

CMD ["./main"]
