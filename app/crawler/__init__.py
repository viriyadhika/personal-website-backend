from flask import Blueprint, request
from .crawler_flask_app.get_batch import handle_get_batch
from .crawler_flask_app.post_batch import handle_post_batch
from .crawler_flask_app.get_batch_details import handle_get_batch_details
from flask_jwt_extended import jwt_required

crawler_blueprint: Blueprint = Blueprint('crawler', __name__, url_prefix='/crawler')

@crawler_blueprint.route('/batch', methods=['GET', 'POST'])
@jwt_required()
def batch():
  if (request.method == 'POST'):
    return handle_post_batch(request.get_json())
  if (request.method == 'GET'):
    return handle_get_batch(request.get_json())
  
@crawler_blueprint.route('/batch/details', methods=['POST'])
def batch_id():
  if (request.method == 'POST'):
    return handle_get_batch_details(request.get_json())