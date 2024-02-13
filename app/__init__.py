from app.env import secret_key
from flask import Flask, request, jsonify
from app.crawler_flask_app.get_batch_id import handle_get_batch_id
from app.crawler_flask_app.get_batch import handle_get_batch
from app.crawler_flask_app.post_batch import handle_post_batch

def create_app():
  app = Flask(__name__)

  app.config.from_mapping(
    SECRET_KEY=secret_key
  )

  @app.route('/batch', methods=['GET', 'POST'])
  def batch():
    if (request.method == 'POST'):
      return handle_post_batch(request.get_json())
    if (request.method == 'GET'):
      return handle_get_batch(request.get_json())
    
  @app.route('/batch/<int:id>', methods=['GET'])
  def batch_id(id):
    if (request.method == 'GET'):
      return handle_get_batch_id(id)
  
  return app