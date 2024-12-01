package services

import (
	"aytorizathion/internal/database"
	"aytorizathion/internal/models"
	"aytorizathion/internal/utils"
	"net/http"

	"github.com/labstack/echo/v4"
)

func RegisterUser(c echo.Context) error {
	var user models.User

	if err := c.Bind(&user); err != nil {
		return c.JSON(http.StatusBadRequest, map[string]string{"error": "Invalid request"})
	}

	hashedPassword, err := utils.HashPassword(user.Password)
	if err != nil {
		return c.JSON(http.StatusInternalServerError, map[string]string{"error": "Error hashing password"})
	}

	user.IsAdmin = false

	_, err = database.DB.Exec("INSERT INTO users(email, password, first_name, last_name, group_name, age, is_admin) VALUES (?, ?, ?, ?, ?, ?, ?)",
		user.Email, hashedPassword, user.FirstName, user.LastName, user.Group, user.Age, user.IsAdmin)

	if err != nil {
		return c.JSON(http.StatusConflict, map[string]string{"error": "User already exists"})
	}

	return c.JSON(http.StatusCreated, map[string]string{"message": "User registered successfully"})
}

func LoginUser(c echo.Context) error {
	var user models.User

	if err := c.Bind(&user); err != nil {
		return c.JSON(http.StatusBadRequest, map[string]string{"error": "Invalid request"})
	}

	var storedUser models.User

	row := database.DB.QueryRow("SELECT password FROM users WHERE email = ?", user.Email)

	if err := row.Scan(&storedUser.Password); err != nil {
		return c.JSON(http.StatusUnauthorized, map[string]string{"error": "Invalid credentials"})
	}

	if !utils.CheckPasswordHash(user.Password, storedUser.Password) {
		return c.JSON(http.StatusUnauthorized, map[string]string{"error": "Invalid credentials"})
	}

	tokenString, err := utils.GenerateJWT(user.Email, user.FirstName, user.LastName, user.Group, user.Age)

	if err != nil {
		return c.JSON(http.StatusInternalServerError, map[string]string{"error": "Could not generate token"})
	}

	return c.JSON(http.StatusOK, map[string]interface{}{
		"token":      tokenString,
		"is_admin":   storedUser.IsAdmin,
		"email":      user.Email,
		"first_name": storedUser.FirstName,
		"last_name":  storedUser.LastName,
		"group":      storedUser.Group,
		"age":        storedUser.Age,
	})
}
