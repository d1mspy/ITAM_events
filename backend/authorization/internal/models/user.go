package models

type User struct {
	ID             string
	Email          string
	HashedPassword string
	FirstName      string
	LastName       string
	Age            int
	GroupInfo      string
	IsAdmin        bool
}
