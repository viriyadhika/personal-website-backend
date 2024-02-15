from app.env import SECRET_KEY, SQLALCHEMY_DATABASE_URI, JWT_SECRET_KEY, JWT_ACCESS_TOKEN_EXPIRES
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)

# Supports credentials
CORS(app, supports_credentials=True)

app.config.from_mapping(
  SECRET_KEY=SECRET_KEY,
  SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI,
  JWT_ACCESS_TOKEN_EXPIRES=JWT_ACCESS_TOKEN_EXPIRES,
  JWT_SECRET_KEY=JWT_SECRET_KEY,
  JWT_TOKEN_LOCATION=['cookies']
)

from app.crawler import crawler_blueprint
app.register_blueprint(crawler_blueprint)

from app.auth import auth_blueprint
app.register_blueprint(auth_blueprint)

jwt = JWTManager(app)