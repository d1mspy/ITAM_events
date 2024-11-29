package config

import (
	"encoding/json"
	"os"
)

type Config struct {
	Database struct {
		Host         string `json:"host"`
		Port         int    `json:"port"`
		Username     string `json:"username"`
		Password     string `json:"password"`
		DatabaseName string `json:"database_name"`
	} `json:"database"`
	SecretKeys struct {
		JWTSecret string `json:"jwt_secret"`
		APIKey    string `json:"api_key"`
	} `json:"secret_keys"`
}

func LoadConfig(filePath string) (*Config, error) {
	configFile, err := os.Open(filePath)
	if err != nil {
		return nil, err
	}
	defer configFile.Close()

	var config Config
	decoder := json.NewDecoder(configFile)
	if err := decoder.Decode(&config); err != nil {
		return nil, err
	}

	return &config, nil
}
