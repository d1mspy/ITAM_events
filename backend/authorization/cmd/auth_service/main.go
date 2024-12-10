package main

import (
	"authorization/internal/config"
	"authorization/internal/db"
	"authorization/internal/handlers"
	"log"
	"net/http"
)

func main() {

	cfg := config.LoadConfig()

	database, err := db.NewDB("myapp.db")
	if err != nil {
		log.Fatalf("Не удалось инициализировать БД: %v", err)
	}

	authHandler := handlers.NewAuthHandler(database, cfg)

	http.HandleFunc("/register", authHandler.RegisterHandler)
	http.HandleFunc("/login", authHandler.LoginHandler)

	log.Println("Сервер запущен на :8080")
	err = http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatalf("Ошибка запуска сервера: %v", err)
	}
}
