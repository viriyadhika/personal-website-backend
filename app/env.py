from dotenv import load_dotenv
from datetime import timedelta
import os

load_dotenv(verbose=True, override=True)

CRAWLER_TOPIC = os.getenv("CRAWLER_TOPIC")
SECRET_KEY = os.getenv("SECRET_KEY")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=60)
KAFKA_HOST = os.getenv("KAFKA_HOST")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB_NAME = os.getenv("POSTGRES_DB")
