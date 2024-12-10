package handlers

import (
	"bytes"
	"encoding/json"
	"io"
	"log"
	"net/http"
	"strings"

	"authorization/internal/config"
	"authorization/internal/db"
	"authorization/internal/models"
	"authorization/internal/services"
	"authorization/internal/utils"
)

type AuthHandler struct {
	db  *db.DB
	cfg *config.Config
}

func NewAuthHandler(database *db.DB, cfg *config.Config) *AuthHandler {
	return &AuthHandler{
		db:  database,
		cfg: cfg,
	}
}

type RegisterRequest struct {
	Email     string `json:"email"`
	Password  string `json:"password"`
	FirstName string `json:"first_name"`
	LastName  string `json:"last_name"`
	Age       int    `json:"age"`
	Group     string `json:"group"`
}

type RegisterResponse struct {
	AccessToken  string `json:"access_token"`
	RefreshToken string `json:"refresh_token"`
}

func (h *AuthHandler) RegisterHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "Только POST метод разрешён", http.StatusMethodNotAllowed)
		return
	}

	body, err := io.ReadAll(r.Body)
	if err != nil {
		log.Printf("Error reading request body: %v", err)
		http.Error(w, "Не удалось прочитать тело запроса", http.StatusBadRequest)
		return
	}

	var req RegisterRequest
	err = json.Unmarshal(body, &req)
	if err != nil {
		log.Printf("Error unmarshalling JSON: %v", err)
		http.Error(w, "Некорректный JSON", http.StatusBadRequest)
		return
	}

	if !utils.IsValidEmail(req.Email) {
		http.Error(w, "Невалидный email", http.StatusBadRequest)
		return
	}

	userID := strings.Split(req.Email, "@")[0]

	hashedPass, err := services.HashPassword(req.Password)
	if err != nil {
		log.Printf("Error hashing password: %v", err)
		http.Error(w, "Ошибка хеширования пароля", http.StatusInternalServerError)
		return
	}

	user := &models.User{
		ID:             userID,
		Email:          req.Email,
		HashedPassword: hashedPass,
		FirstName:      req.FirstName,
		LastName:       req.LastName,
		Age:            req.Age,
		GroupInfo:      req.Group,
		IsAdmin:        false,
	}

	err = h.db.CreateUser(user)
	if err != nil {
		log.Printf("Database error: %v", err)
		http.Error(w, "Не удалось создать пользователя в БД (возможно такой email уже есть)", http.StatusInternalServerError)
		return
	}

	resp := RegisterResponse{}

	resp.AccessToken, _ = services.GenerateAccessToken(user.ID, user.IsAdmin, h.cfg.JWTSecret)

	resp.RefreshToken, _ = services.GenerateRefreshToken(user.ID, h.cfg.JWTSecret)

	go func() {
		pyData := map[string]interface{}{
			"id":         user.ID,
			"email":      user.Email,
			"first_name": user.FirstName,
			"last_name":  user.LastName,
			"age":        user.Age,
			"group":      user.GroupInfo,
			"is_admin":   user.IsAdmin,
		}

		pyBody, _ := json.Marshal(pyData)

		_, _ = http.Post(h.cfg.PythonEndpoint, "application/json", bytes.NewBuffer(pyBody))
	}()

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(resp)
}

type LoginRequest struct {
	Email    string `json:"email"`
	Password string `json:"password"`
}

type LoginResponse struct {
	AccessToken  string `json:"access_token"`
	RefreshToken string `json:"refresh_token"`
}

func (h *AuthHandler) LoginHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "Только POST метод разрешён", http.StatusMethodNotAllowed)
		return
	}

	body, err := io.ReadAll(r.Body)
	if err != nil {
		log.Printf("Error reading request body: %v", err)
		http.Error(w, "Не удалось прочитать тело запроса", http.StatusBadRequest)
		return
	}

	var req LoginRequest
	err = json.Unmarshal(body, &req)
	if err != nil {
		log.Printf("Error unmarshalling JSON: %v", err)
		http.Error(w, "Некорректный JSON", http.StatusBadRequest)
		return
	}

	user, err := h.db.GetUserByEmail(req.Email)
	if err != nil {
		log.Printf("User not found: %v", err)
		http.Error(w, "Пользователь не найден", http.StatusUnauthorized)
		return
	}

	if !services.CheckPasswordHash(req.Password, user.HashedPassword) {
		http.Error(w, "Неправильный пароль", http.StatusUnauthorized)
		return
	}

	resp := LoginResponse{}

	resp.AccessToken, _ = services.GenerateAccessToken(user.ID, user.IsAdmin, h.cfg.JWTSecret)

	resp.RefreshToken, _ = services.GenerateRefreshToken(user.ID, h.cfg.JWTSecret)

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(resp)

}
