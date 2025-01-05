from pydantic import BaseModel


class SignUpRequest(BaseModel):
    username: str
    password: str


class SignUpResponse(BaseModel):
    status: str
