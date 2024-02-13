from dotenv import load_dotenv
import os

load_dotenv()

db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
crawler_topic = os.getenv('CRAWLER_TOPIC')
secret_key = os.getenv('SECRET_KEY')