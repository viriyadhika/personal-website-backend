from app.env import secret_key
from flask import Flask

def create_app():
  app = Flask(__name__)

  app.config.from_mapping(
    SECRET_KEY=secret_key
  )

  @app.route('/hello')
  def hello():
    return 'Hello world'
  
  return app