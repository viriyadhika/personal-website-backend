from app.crawler.crawler_module.mq.event_model import CompanyEvent
from app.crawler.crawler_module.utils.utils import generate_company_file
from app.crawler.crawler_module.utils.file import delete_file
from app.crawler.crawler_module.parser.company import parse_company
from app.crawler.crawler_module.crawler.company import collect_company
from app.crawler.db.company.insert import enrich_company


def handle_company_consumer(event: CompanyEvent):
  collect_company(generate_company_file(event.company_id), event.url)
  company = parse_company(event.company_id, generate_company_file(event.company_id))
  enrich_company(company)
  delete_file(generate_company_file(event.company_id))