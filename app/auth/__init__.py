from flask import Blueprint, request
from .services.signup import signup as signupservice
from .services.login import login as loginservice
from .dto.sign_up_request import SignUpRequest
from .dto.log_in_request import LogInRequest

auth_blueprint: Blueprint = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_blueprint.route('/signup', methods=['POST'])
def signup() -> str:
    return signupservice(SignUpRequest(request.get_json()))


@auth_blueprint.route('/login', methods=['POST'])
def login() -> str:
    return loginservice(LogInRequest(request.get_json()))
