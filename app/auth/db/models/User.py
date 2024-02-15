from ...db import db
from sqlalchemy import Column, Integer, String, LargeBinary


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True)
    password = Column(LargeBinary(64))
    salt = Column(LargeBinary(64))
    role = Column(String(30))

    def __init__(self, username, password, salt, role):
        self.username = username
        self.password = password
        self.salt = salt
        self.role = role

    def __repr__(self) -> str:
        return f'<User {self.username}>'
