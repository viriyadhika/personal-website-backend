from app.crawler.env import secret_key
from flask import Flask
from app.crawler import crawler_blueprint

def create_app():
  app = Flask(__name__)

  app.config.from_mapping(
    SECRET_KEY=secret_key
  )

  app.register_blueprint(crawler_blueprint)
  
  return app