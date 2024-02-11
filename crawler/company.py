import requests
import time
from utils.utils import generate_company_file
from utils.file import safe_open_w

def collect_company(company_id, url):
  response = requests.get(url, headers={ 
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36' 
  })  
  with safe_open_w(generate_company_file(company_id)) as f:
    f.write(response.text)
  time.sleep(5)