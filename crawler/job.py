import requests
import time
from utils.utils import generate_input_file
from utils.file import safe_open_w

def collect_job(input_file_name: str, number_of_job_pages_crawled: int):
  for i in range(number_of_job_pages_crawled):
    response = requests.get('https://www.linkedin.com/jobs/search', { 'start': i * 25, 'position': 1, 'pageNum': 0, 'location': 'Singapore', 'keywords': 'Software Engineer' })  
    with safe_open_w(generate_input_file(input_file_name, i)) as f:
      f.write(response.text)
    time.sleep(5)