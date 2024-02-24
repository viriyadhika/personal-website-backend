from dotenv import load_dotenv
from datetime import timedelta
import os

load_dotenv(verbose=True, override=True)

MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
CRAWLER_TOPIC = os.getenv('CRAWLER_TOPIC')
SECRET_KEY = os.getenv('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=60)
KAFKA_HOST = os.getenv('KAFKA_HOST')
MYSQL_DATABASE=os.getenv('MYSQL_DATABASE')
MYSQL_HOST=os.getenv('MYSQL_HOST')