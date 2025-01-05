from fastapi import HTTPException

from app.crawler.api.dto.post_batch import PostBatchRequest
from app.crawler.crawler_module import main_producer


def handle_post_batch(payload: PostBatchRequest):
    try:
        main_producer.run(payload.location, payload.keywords)
        return {}
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))
