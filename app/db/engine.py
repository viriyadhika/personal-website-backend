from sqlalchemy import create_engine
from app.env import POSTGRES_PASSWORD, POSTGRES_DB_NAME, POSTGRES_HOST, POSTGRES_USER

engine = create_engine(
    f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB_NAME}"
)
