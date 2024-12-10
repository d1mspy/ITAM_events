package config

type Config struct {
	JWTSecret      []byte
	PythonEndpoint string
}

func LoadConfig() *Config {
	return &Config{
		JWTSecret:      []byte("supersecretkey"),
		PythonEndpoint: "http://localhost:8000/register",
	}
}
