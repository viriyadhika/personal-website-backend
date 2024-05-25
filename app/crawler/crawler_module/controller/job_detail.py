from app.crawler.crawler_module.crawler.job_detail import collect_job_detail
from app.crawler.crawler_module.mq.event_model import JobDetailEvent
from app.crawler.crawler_module.parser.job_detail import parse_job_detail
from app.crawler.crawler_module.utils.file import delete_file
from app.crawler.crawler_module.utils.utils import generate_job_detail_file
from app.crawler.db.job.insert import can_enhance_job, enrich_job


def handle_job_detail_consumer(event: JobDetailEvent):
    if not can_enhance_job(event.job_id):
        return
    try:
        collect_job_detail(generate_job_detail_file(event.job_id), event.url)
        company = parse_job_detail(event.job_id, generate_job_detail_file(event.job_id))
        enrich_job(company)
    except Exception as err:
        print(f"Error getting company {event.job_id} {err}")
    finally:
      try:
          delete_file(generate_job_detail_file(event.job_id))
      except Exception as err:
          print(f"File is not there, cannot delete {event.job_id}")
