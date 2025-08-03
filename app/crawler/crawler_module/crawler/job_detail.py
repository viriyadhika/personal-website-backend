import requests
import time
from app.crawler.crawler_module.utils.file import safe_open_w
import random


def collect_job_detail(job_detail_url: str, url: str):
    response = requests.get(
        url,
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        },
    )
    with safe_open_w(job_detail_url) as f:
        f.write(response.text)
    time.sleep(random.randint(5, 20))
