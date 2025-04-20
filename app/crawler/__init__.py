from typing import Annotated
from fastapi import APIRouter, Depends

from app.common.auth.jwt import get_current_user
import asyncio

from .crawler_module.crawler.ptime import crawl_ptime
from .crawler_module.main_consumer import MainConsumer
from .api.dto.get_batch_details import GetBatchDetailRequest
from .api.dto.post_batch import PostBatchRequest
from .api.dto.get_ptime import PtimeRequest, PtimeResponse
from .api.get_batch import handle_get_batch
from .api.post_batch import handle_post_batch
from .api.get_batch_details import handle_get_batch_details
from .api.get_ptime import get_ptime
from .crawler_module import main_producer, create_topic
from .db.batch import get_all_batch
from app.common.scheduler import scheduler

crawler_router = APIRouter(prefix="/api/crawler")


@crawler_router.post("/batch")
def batch(
    request: PostBatchRequest, current_user: Annotated[str, Depends(get_current_user)]
):
    return handle_post_batch(request)


@crawler_router.get("/batch")
def get_batch():
    return handle_get_batch()


@crawler_router.post("/batch/details")
def batch_id(request: GetBatchDetailRequest):
    return handle_get_batch_details(request)


@crawler_router.post("/ptime")
def ptime(request: PtimeRequest) -> list[PtimeResponse]:
    return get_ptime(request)


@scheduler.scheduled_job("cron", hour=0, minute=0)
def refresh_batches():
    all_batches = get_all_batch()
    for batch in all_batches:
        main_producer.run(batch.location, batch.keywords)


@scheduler.scheduled_job("cron", day_of_week="fri", hour=0, minute=0)
def refresh_ptime():
    crawl_ptime()


def init_crawler():
    create_topic.run()
    c = MainConsumer()
    kafka_task = asyncio.create_task(asyncio.to_thread(c.run))

    def close():
        c.close()
        kafka_task.cancel()

    return close
