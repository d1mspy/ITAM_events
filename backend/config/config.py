import os

JWT_SECRET = os.environ['JWT_SECRET']
DB_URL = 'sqlite+aiosqlite:///backend/sqlite.db'