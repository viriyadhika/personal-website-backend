from dotenv import load_dotenv
import os

load_dotenv(verbose=True, override=True)

CRAWLER_TOPIC = os.getenv("CRAWLER_TOPIC")
SECRET_KEY = os.getenv("SECRET_KEY")
KAFKA_HOST = os.getenv("KAFKA_HOST")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB_NAME = os.getenv("POSTGRES_DB")
ALLOWED_ORIGIN = os.getenv("ALLOWED_ORIGIN")
PTIME_URL = os.getenv("PTIME_URL")
PTIME_NON_CTRY_URL = os.getenv("PTIME_NON_CTRY_URL")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
