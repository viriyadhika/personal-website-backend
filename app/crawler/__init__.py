from flask import Blueprint, request
from .crawler_flask_app.get_batch import handle_get_batch
from .crawler_flask_app.post_batch import handle_post_batch
from .crawler_flask_app.get_batch_id import handle_get_batch_id

crawler_blueprint: Blueprint = Blueprint('crawler', __name__, url_prefix='/crawler')

@crawler_blueprint.route('/batch', methods=['GET', 'POST'])
def batch():
  if (request.method == 'POST'):
    return handle_post_batch(request.get_json())
  if (request.method == 'GET'):
    return handle_get_batch(request.get_json())
  
@crawler_blueprint.route('/batch/<int:id>', methods=['GET'])
def batch_id(id):
  if (request.method == 'GET'):
    return handle_get_batch_id(id)