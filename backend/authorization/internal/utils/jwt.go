package utils

import (
	"time"

	"github.com/dgrijalva/jwt-go"
)

type UserClaims struct {
	Email     string `json:"email"`
	FirstName string `json:"first_name"`
	LastName  string `json:"last_name"`
	Group     string `json:"group"`
	Age       int    `json:"age"`
	jwt.StandardClaims
}

var secretKey []byte

func InitializeSecretKey(key string) {
	secretKey = []byte(key)
}

func GenerateJWT(email, firstName, lastName, group string, age int) (string, error) {
	claims := &UserClaims{
		Email:     email,
		FirstName: firstName,
		LastName:  lastName,
		Group:     group,
		Age:       age,
		StandardClaims: jwt.StandardClaims{
			ExpiresAt: time.Now().Add(time.Hour * 72).Unix(),
		},
	}

	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
	return token.SignedString(secretKey)
}

func ValidateJWT(tokenString string) (*UserClaims, error) {
	claims := &UserClaims{}
	token, err := jwt.ParseWithClaims(tokenString, claims, func(token *jwt.Token) (interface{}, error) {
		return secretKey, nil
	})

	if err != nil || !token.Valid {
		return nil, err
	}

	return claims, nil
}
