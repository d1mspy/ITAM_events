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
	cfg, err := config.LoadConfig("config.json")
	if err != nil {
		log.Fatalf("Could not load config: %v", err)
	}

	utils.InitializeSecretKey(cfg.SecretKeys.JWTSecret)

	if err := database.InitDB(cfg); err != nil {
		log.Fatalf("Could not initialize database: %v", err)
	}

	e := echo.New()

	e.POST("/register", services.RegisterUser)
	e.POST("/login", services.LoginUser)

	log.Println("Server is running on port 8080")
	log.Fatal(e.Start(":8080"))
}
