from typing import Annotated
from fastapi import APIRouter, Depends

from app.common.auth.jwt import get_current_user
from .api.dto.get_batch_details import GetBatchDetailRequest
from .api.dto.post_batch import PostBatchRequest
from .api.get_batch import handle_get_batch
from .api.post_batch import handle_post_batch
from .api.get_batch_details import handle_get_batch_details

crawler_router = APIRouter(prefix="/api/crawler")


@crawler_router.post("/batch")
def batch(
    request: PostBatchRequest, current_user: Annotated[str, Depends(get_current_user)]
):
    return handle_post_batch(request)


@crawler_router.get("/batch")
def get_all_batch():
    return handle_get_batch()


@crawler_router.post("/batch/details")
def batch_id(request: GetBatchDetailRequest):
    return handle_get_batch_details(request)
