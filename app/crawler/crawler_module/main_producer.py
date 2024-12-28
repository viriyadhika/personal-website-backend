from app.crawler.crawler_module.mq.producer import queue_job_search
from app.crawler.crawler_module.utils.utils import generate_batch_id
from app.crawler.model.batch import BatchDto
from app.crawler.db.batch import insert_or_update_batch


def run(location: str, keywords: str):
    try:
        batch = BatchDto(
            batch_id=generate_batch_id(location, keywords),
            location=location,
            keywords=keywords,
        )
        insert_or_update_batch(batch)
    except Exception as err:
        print(f"Encountered exception {err}")
        pass
    queue_job_search(location, keywords)
