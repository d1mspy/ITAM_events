package models

type User struct {
    Email     string `json:"email"`
    Password  string `json:"password"`
    FirstName string `json:"first_name"`
    LastName  string `json:"last_name"`
    Group     string `json:"group"` 
    Age       int    `json:"age"`   
    IsAdmin   bool   `json:"is_admin"` 
}
