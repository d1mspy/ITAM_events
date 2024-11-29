package database

import (
	"aytorizathion/internal/config"
	"database/sql"
	"log"
	"os"

	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/database/sqlite3"
	_ "github.com/golang-migrate/migrate/v4/source/file" // Importing file source for migrations
	_ "github.com/mattn/go-sqlite3"                      // Importing SQLite driver
)

// DB is a global variable for the database connection.
var DB *sql.DB

// InitDB initializes the SQLite database and runs migrations.
func InitDB(cfg *config.Config) error {
	var err error

	DB, err = sql.Open("sqlite3", "./users.db")
	if err != nil {
		return err
	}

	if err := runMigrations(); err != nil {
		return err
	}

	return nil
}

// runMigrations applies all pending migrations.
func runMigrations() error {
	driver, err := sqlite3.WithInstance(DB, &sqlite3.Config{})
	if err != nil {
		return err
	}

	migrationsPath := "file://" + os.Getenv("PWD") + "/internal/database/migrations"
	m, err := migrate.NewWithDatabaseInstance(migrationsPath, "sqlite3", driver)
	if err != nil {
		return err // Return error if migration instance creation fails.
	}

	if err := m.Up(); err != nil && err != migrate.ErrNoChange {
		return err // Return error if migration fails.
	}

	log.Println("Migrations applied successfully.")
	return nil
}
