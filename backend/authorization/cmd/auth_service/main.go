package main

import (
	"authorization/internal/config"
	"authorization/internal/db"
	"authorization/internal/handlers"
	"log"
	"net/http"
)

func enableCORS(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Access-Control-Allow-Origin", "*")
		w.Header().Set("Access-Control-Allow-Methods", "POST, GET, OPTIONS, PUT, DELETE")
		w.Header().Set("Access-Control-Allow-Headers", "Content-Type, Authorization")

		if r.Method == "OPTIONS" {
			return
		}

		next.ServeHTTP(w, r)
	})
}

func main() {
	cfg := config.LoadConfig()

	database, err := db.NewDB("myapp.db")
	if err != nil {
		log.Fatalf("Не удалось инициализировать БД: %v", err)
	}

	authHandler := handlers.NewAuthHandler(database, cfg)

	http.Handle("/register", enableCORS(http.HandlerFunc(authHandler.RegisterHandler)))
	http.Handle("/login", enableCORS(http.HandlerFunc(authHandler.LoginHandler)))

	log.Println("Сервер запущен на :8080")
	err = http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatalf("Ошибка запуска сервера: %v", err)
	}
}
