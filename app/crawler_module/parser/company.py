from bs4 import BeautifulSoup
from app.model.company import Company

def parse_company(company_id: str, input_file: str):
  with open(input_file) as f:
    soup = BeautifulSoup(f, 'html.parser')
    container = soup.find('div', attrs={'data-test-id': 'about-us__size'})
    employee = container.find_next('dd').text.strip()
    return Company(company_id, employee=employee)