from bs4 import BeautifulSoup
from app.crawler.model.job import JobDto


def parse_job_detail(job_id: str, input_file: str):
    with open(input_file) as f:
        soup = BeautifulSoup(f, "html.parser")
        container = soup.find("div", class_="description__text description__text--rich")
        description = ""
        for descendant in container.descendants:
            description += descendant.get_text().strip()
        return JobDto(
            job_id,
            description=description[max(0, len(description) - 2990) : len(description)],
        )
