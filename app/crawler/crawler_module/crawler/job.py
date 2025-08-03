import requests
import time
from app.crawler.crawler_module.utils.utils import generate_input_file
from app.crawler.crawler_module.utils.file import safe_open_w
from dataclasses import dataclass


@dataclass
class Payload:
    keywords: str
    location: str


def collect_job(
    input_file_name: str, number_of_job_pages_crawled: int, payload: Payload
):
    print(f"Gettting job {0} for payload {payload}")
    common_payload = {"geoId": "", "trk": "public_jobs_jobs-search-bar_search-submit"}
    response = requests.get(
        "https://www.linkedin.com/jobs/search",
        {**common_payload, "keywords": payload.keywords, "location": payload.location},
    )
    print(f"Response for job 0 obtained {response}")
    with safe_open_w(generate_input_file(input_file_name, 0)) as f:
        f.write(response.text)
        print("Writing finish")
        time.sleep(5)

    for i in range(1, number_of_job_pages_crawled):
        print(f"Gettting job {i} for payload {payload}")
        default_param = {"start": str(i * 25 + 25)}
        response = requests.get(
            "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search",
            {
                **default_param,
                **common_payload,
                "keywords": payload.keywords.replace(" ", "+"),
                "location": payload.location,
            },
        )
        with safe_open_w(generate_input_file(input_file_name, i)) as f:
            f.write(response.text)
        time.sleep(5)
