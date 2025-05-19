# ITAM events
**ITAM events**  — сервис управления мероприятиями, созданный командой разработчиков 

## Contributors

- [@d1mspy](https://github.com/d1mspy) — FastAPI backend, Docker, Nginx
- [@Polina1HEG](https://github.com/Polina1HEG) — Svelte frontend, интеграция с API
- [@klarness](https://github.com/klarness) — Go Auth-сервис, JWT-логика
- [@METALROK](https://github.com/METALROK) — FastAPI backend, email service

## Структура проекта
#### Auth Service (Go Gin)

- JWT-авторизация и аутентификация  
- Хранение хешей паролей
- Выдача JWT

#### Main API (Python FastAPI)

- Валидация JWT и определение роли (user/admin)
- Все необходимые операции над мероприятиями
- Отправка email-оповещений

#### Frontend (Svelte)

- Страница авторизации
- Страницы мероприятий
- Админ-панель


