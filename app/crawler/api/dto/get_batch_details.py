from typing import Optional
from pydantic import BaseModel


class GetBatchDetailRequest(BaseModel):
    id: str
    timestamp: int
    comparison_timestamp: int


class GetBatchDetailResponse(BaseModel):
    company: str
    job_id: str
    job_name: str
    link: str
    description: str
    employee: Optional[str]
    is_new: bool
