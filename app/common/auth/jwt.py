from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import Depends, HTTPException
from app.common.dto.user import UserDto
from app.env import (
    SECRET_KEY,
)

import jwt
from jwt.exceptions import InvalidTokenError
from fastapi.security import OAuth2PasswordBearer

ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def create_access_token(identity: str, role: str):
    to_encode: dict = {"sub": identity}
    expire = datetime.now(timezone.utc) + timedelta(days=60)
    to_encode.update({"exp": expire})
    to_encode.update({"role": role})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            options={"require": ["sub", "exp", "role"]},
            algorithms=[ALGORITHM],
        )
        return UserDto(username=payload.get("sub"), role=payload.get("role"))
    except InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
