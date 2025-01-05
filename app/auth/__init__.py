from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from .services.signup import signup as signupservice
from .services.login import login as loginservice
from .dto.sign_up_request import SignUpRequest, SignUpResponse
from .dto.log_in_request import LogInResponse
from fastapi import APIRouter, Depends, Response


auth_router = APIRouter(prefix="/api/auth")


@auth_router.post("/signup")
def signup(sign_up_request: SignUpRequest) -> SignUpResponse:
    return signupservice(sign_up_request)


@auth_router.post("/login")
def login(
    log_in_request: Annotated[OAuth2PasswordRequestForm, Depends()], response: Response
) -> LogInResponse:
    result = loginservice(log_in_request)

    response.set_cookie("access_token_cookie", value=result.access_token)
    return result
