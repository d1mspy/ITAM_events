import os
from dotenv import load_dotenv

load_dotenv()

SERVER_EMAIL_ADDRESS = str(os.getenv('SERVER_EMAIL_ADDRESS')) 
SERVER_EMAIL_PASSWORD = str(os.getenv('SERVER_EMAIL_PASSWORD'))  
JWT_SECRET = str(os.getenv('JWT_SECRET'))
DB_URL = 'sqlite+aiosqlite:///backend/event_logic/sqlite.db'