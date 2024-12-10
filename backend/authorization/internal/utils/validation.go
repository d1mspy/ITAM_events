package utils

import (
	"net/mail"
	"strings"
)

// IsValidEmail проверяет формат email.
func IsValidEmail(email string) bool {
	if len(email) == 0 || !strings.Contains(email, "@") {
		return false
	}
	_, err := mail.ParseAddress(email)
	return err == nil
}
