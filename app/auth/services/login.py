from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from ..dto.log_in_request import LogInResponse
from ..db.models.User import User
from ..utils.password_hash import hash_password
from sqlalchemy import select
from app.db.engine import engine
from sqlalchemy.orm import Session
from app.common.auth.jwt import create_access_token


def login(request: OAuth2PasswordRequestForm):
    try:
        with Session(engine) as session:
            statement = select(User).where(User.username == request.username)
            queried_user = session.scalars(statement).first()
    except Exception as ex:
        print(ex)
        raise HTTPException(status_code=500, detail="Something went wrong")

    if queried_user is None:
        raise HTTPException(status_code=401, detail="Username or password is wrong")

    if hash_password(request.password, queried_user.salt) != queried_user.password:
        raise HTTPException(status_code=401, detail="Username or password is wrong")

    access_token = create_access_token(identity=request.username)
    return LogInResponse(access_token=access_token)
