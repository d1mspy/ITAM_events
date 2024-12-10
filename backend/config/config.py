import os

JWT_SECRET = os.getenv('JWT_SECRET')
DB_URL = 'sqlite+aiosqlite:///backend/sqlite.db'