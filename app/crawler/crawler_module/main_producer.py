from app.crawler.crawler_module.mq.producer import queue_job_search
from app.crawler.crawler_module.utils.utils import generate_batch_id
from app.crawler.model.batch import Batch, Status
from app.crawler.db.batch import insert_batch

def run(location: str, keywords: str):
  try:
    batch = Batch(generate_batch_id(location, keywords), Status.QUEUING)
    insert_batch(batch)
  except Exception as err:
    print(f'Encountered exception {err}')
    pass
  queue_job_search(location, keywords)
