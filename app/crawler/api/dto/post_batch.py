from pydantic import BaseModel


class PostBatchRequest(BaseModel):
    keywords: str
    location: str
