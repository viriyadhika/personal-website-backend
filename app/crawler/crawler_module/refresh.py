import time
from .main_producer import run
from app.crawler.db.batch import get_all_batch

def auto_refresh():
    while True:
        try:
            time.sleep(3600 * 24)
            all_batches = get_all_batch()
            for batch in all_batches:
                run(batch.location, batch.keywords)
        except Exception as exc:
            print(exc)