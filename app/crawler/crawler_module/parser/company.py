from bs4 import BeautifulSoup
from app.crawler.model.company import CompanyDto


def parse_company(company_id: str, input_file: str):
    with open(input_file) as f:
        soup = BeautifulSoup(f, "html.parser")
        container = soup.find("div", attrs={"data-test-id": "about-us__size"})
        employee = container.find_next("dd").text.strip()
        return CompanyDto(company_id, employee=employee)
