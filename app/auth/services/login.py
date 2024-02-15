from ..dto.log_in_request import LogInRequest
from ..db.models.User import User
from ..utils.password_hash import hash_password
from ..utils.error_message import create_error_message
from flask import abort, make_response, jsonify
from flask_jwt_extended import create_access_token, set_access_cookies


def login(request: LogInRequest):
    try:
        queried_user: User = User.query.filter_by(
            username=request.username).first()
    except:
        abort(make_response(create_error_message('Something went wrong'), 500))

    if (queried_user == None or hash_password(request.password, queried_user.salt) != queried_user.password):
        abort(make_response(create_error_message(
            'Username or password is wrong'), 401))
    
    access_token = create_access_token(identity=request.username)
    response = jsonify({'access_token': access_token })
    set_access_cookies(response, access_token)
    return response
