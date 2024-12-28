from ..dto.sign_up_request import SignUpRequest
from ..db.models.User import User
from typing import Dict
from sqlalchemy.exc import IntegrityError
from enum import Enum
from ..utils.password_hash import generate_salt, hash_password
from ..utils.error_message import create_error_message
from flask import abort, make_response
from sqlalchemy.orm import Session
from app.db.engine import engine


class Status(Enum):
    USERNAME_EXIST = "USERNAME_EXIST"
    SUCCESS = "SUCCESS"
    UNKNOWN_ERROR = "UNKNOWN_ERROR"


def signup(request: SignUpRequest) -> Dict[str, str]:
    try:
        salt = generate_salt()
        with Session(engine) as session:
            user: User = User(
                username=request.username,
                password=hash_password(request.password, salt),
                salt=salt,
                role="USER",
            )
            session.add(user)
            session.commit()
    except IntegrityError:
        return abort(make_response(create_error_message("Username already exist"), 400))
    except Exception:
        return abort(make_response(create_error_message("Something went wrong"), 500))

    return {"response": "Success"}
