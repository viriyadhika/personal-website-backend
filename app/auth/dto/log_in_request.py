from pydantic import BaseModel


class LogInResponse(BaseModel):
    access_token: str
