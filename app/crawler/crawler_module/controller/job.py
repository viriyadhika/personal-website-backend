from app.crawler.crawler_module.crawler.job import collect_job
from app.crawler.crawler_module.utils.constants import NUMBER_OF_JOB_PAGES, INPUT_FILE
from app.crawler.crawler_module.utils.utils import generate_input_file
from app.crawler.crawler_module.utils.file import delete_file
from app.crawler.crawler_module.parser.job import parse_jobs
from app.crawler.db.job.insert import insert_job
from app.crawler.db.company.insert import insert_company
from app.crawler.db.batch_relationship.batch import insert_batch_relationship
from app.crawler.model.batch_relationship import BatchRelationship
from app.crawler.crawler_module.mq.producer import (
    queue_company_search,
    queue_job_detail_search,
)
from app.crawler.crawler_module.mq.event_model import JobEvent


def handle_job_consumer(event: JobEvent):
    try:
        collect_job(INPUT_FILE, NUMBER_OF_JOB_PAGES, event.payload)
    except Exception as err:
        print(f"Error collecting job {err}")
        pass

    for i in range(NUMBER_OF_JOB_PAGES):
        try:
            jobs = parse_jobs(generate_input_file(INPUT_FILE, i))
            for job in jobs:
                insert_company(job.company)
                insert_job(job)
                insert_batch_relationship(BatchRelationship(event.batch_id, job.id))
                queue_company_search(job.company.id, job.company.link)
                queue_job_detail_search(job.id, job.link)
        finally:
            delete_file(generate_input_file(INPUT_FILE, i))
