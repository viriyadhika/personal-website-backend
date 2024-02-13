from bs4 import BeautifulSoup
from app.model.company import Company
from app.model.job import Job
from typing import List

def get_job_id(url):
  host = url.split('?')[0]
  return host.split('-')[-1]

def get_company_id(url):
  host = url.split('?')[0]
  return host.split('/')[-1]

def parse_jobs(input_file: str, batch_id: str):
  result: List[Job] = []
  with open(input_file) as f:
    soup = BeautifulSoup(f, 'html.parser')
    containers = soup.find_all('div', class_='base-card')
    for container in containers:
      title = container.find_next('h3', class_='base-search-card__title').text.strip()
      link = container.find_next('a', class_='base-card__full-link')['href']
      company_soup = container.find_next('h4', class_='base-search-card__subtitle').find_next('a')
      company_name = company_soup.text.strip()
      company_link = company_soup['href']
      company = Company(get_company_id(company_link), company_name, company_link)
      job = Job(get_job_id(link), title, company, link, batch_id)

      result.append(job)

  return result
