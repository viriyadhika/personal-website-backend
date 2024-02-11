import requests
import time
from ..utils.utils import generate_input_file
from ..utils.file import safe_open_w

def collect_job(input_file_name: str, number_of_job_pages_crawled: int, payload: dict):
  print(f'Gettting job {0} for payload {payload}')
  response = requests.get('https://www.linkedin.com/jobs/search', { 'start': 0, 'position': 1, **payload })
  with safe_open_w(generate_input_file(input_file_name, 0)) as f:
    f.write(response.text)
    time.sleep(5)
  
  for i in range(1, number_of_job_pages_crawled):
    print(f'Gettting job {i} for payload {payload}')
    default_param = { 'start': i * 25, 'position': 1, 'pageNum': 0 }
    response = requests.get('https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search', { **default_param, **payload })
    with safe_open_w(generate_input_file(input_file_name, i)) as f:
      f.write(response.text)
    time.sleep(5)