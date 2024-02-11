from ..mq.event_model import CompanyEvent
from ..utils.utils import generate_company_file
from ..utils.file import delete_file
from ..parser.company import parse_company
from ..crawler.company import collect_company
from db.company.insert import enrich_company


def handle_company_consumer(event: CompanyEvent):
  collect_company(generate_company_file(event.company_id), event.url)
  company = parse_company(event.company_id, generate_company_file(event.company_id))
  enrich_company(company)
  delete_file(generate_company_file(event.company_id))