package db

import (
	"authorization/internal/models"
	"database/sql"

	_ "github.com/mattn/go-sqlite3"
)

// DB – структура для работы с базой данных.
type DB struct {
	conn *sql.DB
}

// NewDB открывает или создаёт файл БД, создаёт таблицы, если их нет.
func NewDB(path string) (*DB, error) {
	conn, err := sql.Open("sqlite3", path)
	if err != nil {
		return nil, err
	}

	// Создаём таблицу users, если не существует
	createTable := `CREATE TABLE IF NOT EXISTS users (
		id TEXT PRIMARY KEY,
		email TEXT UNIQUE NOT NULL,
		hashed_password TEXT NOT NULL,
		first_name TEXT NOT NULL,
		last_name TEXT NOT NULL,
		age INTEGER NOT NULL,
		group_info TEXT NOT NULL,
		is_admin BOOLEAN NOT NULL DEFAULT 0
	);`

	_, err = conn.Exec(createTable)
	if err != nil {
		return nil, err
	}

	return &DB{conn: conn}, nil
}

// CreateUser вставляет нового пользователя в БД.
func (d *DB) CreateUser(u *models.User) error {
	stmt := `INSERT INTO users (id, email, hashed_password, first_name, last_name, age, group_info, is_admin)
	VALUES (?, ?, ?, ?, ?, ?, ?, ?);`
	_, err := d.conn.Exec(stmt,
		u.ID,
		u.Email,
		u.HashedPassword,
		u.FirstName,
		u.LastName,
		u.Age,
		u.GroupInfo,
		false) // Устанавливаем is_admin по умолчанию как false
	return err
}

// GetUserByEmail получает пользователя по email.
func (d *DB) GetUserByEmail(email string) (*models.User, error) {
	stmt := `SELECT id, email, hashed_password, first_name, last_name, age, group_info, is_admin FROM users WHERE email = ?;`
	row := d.conn.QueryRow(stmt, email)

	var user models.User
	err := row.Scan(&user.ID, &user.Email, &user.HashedPassword, &user.FirstName, &user.LastName, &user.Age, &user.GroupInfo, &user.IsAdmin)
	if err != nil {
		return nil, err
	}

	return &user, nil
}
