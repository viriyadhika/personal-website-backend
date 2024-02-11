from utils.utils import generate_input_file
from utils.constants import NUMBER_OF_JOB_PAGES, INPUT_FILE
from parser.job import get_companies
from crawler.company import collect_company
from crawler.job import collect_job

if __name__ == '__main__':
  collect_job(INPUT_FILE, NUMBER_OF_JOB_PAGES)
  idx = 0
  for i in range(NUMBER_OF_JOB_PAGES):
    jobs = get_companies(generate_input_file(INPUT_FILE, i))
    for job in jobs:
      if (idx < 5):
        collect_company(job.company.id, job.company.link)
        idx += 1
      print(job)
  
