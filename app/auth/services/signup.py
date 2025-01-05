from fastapi import HTTPException
from ..dto.sign_up_request import SignUpRequest, SignUpResponse
from ..db.models.User import User
from typing import Dict
from sqlalchemy.exc import IntegrityError
from enum import Enum
from ..utils.password_hash import generate_salt, hash_password
from ..utils.error_message import create_error_message

from sqlalchemy.orm import Session
from app.db.engine import engine


class Status(Enum):
    USERNAME_EXIST = "USERNAME_EXIST"
    SUCCESS = "SUCCESS"
    UNKNOWN_ERROR = "UNKNOWN_ERROR"


def signup(request: SignUpRequest) -> SignUpResponse:
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
        raise HTTPException(status_code=400, detail="Username already exist")
    except Exception:
        raise HTTPException(status_code=500, detail="Something went wrong")

    return SignUpResponse(status="success")
