package main

import (
	"aytorizathion/internal/config"
	"aytorizathion/internal/database"
	"aytorizathion/internal/services"
	"aytorizathion/internal/utils"
	"log"

	"github.com/labstack/echo/v4"
)

func main() {
	// Load configuration from config.json
	cfg, err := config.LoadConfig("config.json")
	if err != nil {
		log.Fatalf("Could not load config: %v", err)
	}

	// Initialize JWT secret key from config.
	utils.InitializeSecretKey(cfg.SecretKeys.JWTSecret)

	// Initialize database connection and run migrations using loaded config.
	if err := database.InitDB(cfg); err != nil {
		log.Fatalf("Could not initialize database: %v", err)
	}

	e := echo.New()

	// Define routes for registration and login.
	e.POST("/register", services.RegisterUser)
	e.POST("/login", services.LoginUser)

	log.Println("Server is running on port 8000")
	log.Fatal(e.Start(":8000"))
}
