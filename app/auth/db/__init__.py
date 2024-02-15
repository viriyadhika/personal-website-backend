from flask_sqlalchemy import SQLAlchemy

from app import app

db: SQLAlchemy = SQLAlchemy(app)

def init_auth_db():
  from app.auth.db.models import User
  with app.app_context():
    print("Setting up auth DB")
    db.create_all()
    print("Setting up auth DB success")
