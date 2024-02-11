from utils.utils import generate_input_file
from utils.constants import NUMBER_OF_JOB_PAGES, INPUT_FILE
from parser.job import get_companies
from crawler.company import collect_company
from crawler.job import collect_job
from dumper.job import dump_data
from db.migrate import migrate
from db.job.insert import insert_job
from db.company.insert import insert_company
from model.company import Company
from model.job import Job

if __name__ == '__main__':
  migrate()
  collect_job(INPUT_FILE, NUMBER_OF_JOB_PAGES)
  idx = 0
  for i in range(NUMBER_OF_JOB_PAGES):
    jobs = get_companies(generate_input_file(INPUT_FILE, i))
    for job in jobs:
      if (idx < 5):
        collect_company(job.company.get_id(), job.company.get_link())
        idx += 1
      insert_job(job)
