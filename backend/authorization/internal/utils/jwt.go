package utils

import (
	"time"

	"github.com/dgrijalva/jwt-go"
)

var secretKey []byte

func InitializeSecretKey(key string) {
	secretKey = []byte(key)
}

func GenerateJWT(email, firstName, lastName, group string, age int) (string, error) {
	claims := jwt.MapClaims{}
	claims["email"] = email
	claims["first_name"] = firstName
	claims["last_name"] = lastName
	claims["group"] = group
	claims["age"] = age
	claims["exp"] = time.Now().Add(time.Hour * 72).Unix()

	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
	return token.SignedString(secretKey)
}

func ValidateJWT(tokenString string) (map[string]interface{}, error) {
	token, err := jwt.Parse(tokenString, func(token *jwt.Token) (interface{}, error) {
		return secretKey, nil
	})

	if claims, ok := token.Claims.(jwt.MapClaims); ok && token.Valid {
		return claims, nil
	}

	return nil, err
}
