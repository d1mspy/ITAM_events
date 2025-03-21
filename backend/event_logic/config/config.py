import os
from dotenv import load_dotenv

load_dotenv()

SERVER_EMAIL_ADDRESS = str(os.getenv('SERVER_EMAIL_ADDRESS')) 
SERVER_EMAIL_PASSWORD = str(os.getenv('SERVER_EMAIL_PASSWORD')) 

JWT_SECRET = str(os.getenv('JWT_SECRET'))

PG_USER = str(os.getenv('APP_PG__USER'))
PG_HOST = str(os.getenv('APP_PG__HOST'))
PG_PORT = int(os.getenv('APP_PG__PORT'))
PG_PASSWORD = str(os.getenv('APP_PG__PASSWORD'))
DB = str(os.getenv('APP_PG__DATABASE'))
