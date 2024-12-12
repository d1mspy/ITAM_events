import os
from dotenv import load_dotenv

load_dotenv()

SERVER_EMAIL_ADRESS = str(os.getenv('SERVER_EMAIL_ADRESS')) 
SERVER_EMAIL_PASSWORD = str(os.getenv('SERVER_EMAIL_PASSWORD'))  
JWT_SECRET = str(os.getenv('JWT_SECRET'))
DB_URL = 'sqlite+aiosqlite:///backend/sqlite.db'