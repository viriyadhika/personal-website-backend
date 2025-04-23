from ..db.models.User import User
from sqlalchemy import select
from app.db.engine import engine
from sqlalchemy.orm import Session


def get_user_based_on_username(username: str):
    with Session(engine) as session:
        statement = select(User).where(User.username == username)
        queried_user = session.scalars(statement).first()
        return queried_user
