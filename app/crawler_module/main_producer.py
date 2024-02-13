from app.crawler_module.mq.producer import queue_job_search
from app.crawler_module.utils.utils import generate_batch_id
from app.model.batch import Batch, Status
from app.db.batch import insert_batch

def run():
  location = 'Singapore'
  keywords = 'Software Engineer'
  batch = Batch(generate_batch_id(location, keywords), Status.QUEUING)
  insert_batch(batch)
  queue_job_search(location, keywords)

if __name__ == '__main__':
  run()