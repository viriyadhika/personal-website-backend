from ..crawler.job import collect_job
from ..utils.constants import NUMBER_OF_JOB_PAGES, INPUT_FILE
from ..utils.utils import generate_input_file
from ..utils.file import delete_file
from ..parser.job import parse_jobs
from db.job.insert import insert_job
from db.company.insert import insert_company
from ..mq.producer import queue_company_search
from ..mq.event_model import JobEvent

def handle_job_consumer(event: JobEvent):
  collect_job(INPUT_FILE, NUMBER_OF_JOB_PAGES, event.payload)
  for i in range(NUMBER_OF_JOB_PAGES):
    jobs = parse_jobs(generate_input_file(INPUT_FILE, i))
    for job in jobs:
      insert_company(job.company)
      insert_job(job)
      queue_company_search(job.company.id, job.company.link)
    delete_file(generate_input_file(INPUT_FILE, i))