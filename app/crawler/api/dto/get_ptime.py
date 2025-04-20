from pydantic import BaseModel


class PtimeRequest(BaseModel):
    ctry: str


class PtimeResponse(BaseModel):
    v_type: str
    date: str
    ptime: str
    ctry: str
