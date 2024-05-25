from kafka import KafkaProducer
from app.env import CRAWLER_TOPIC, KAFKA_HOST
from app.crawler.crawler_module.mq.event_model import JobEvent, CompanyEvent, JobDetailEvent
from app.crawler.crawler_module.utils.utils import generate_batch_id

def queue_job_search(location: str, keywords: str):
  producer = KafkaProducer(bootstrap_servers=KAFKA_HOST)
  event = JobEvent(location, keywords, generate_batch_id(location, keywords))
  producer.send(CRAWLER_TOPIC, value=event.get_event_value())
  producer.flush()

def queue_company_search(company_id: str, url: str):
  producer = KafkaProducer(bootstrap_servers=KAFKA_HOST)
  event = CompanyEvent(company_id, url)
  producer.send(CRAWLER_TOPIC, value=event.get_event_value())
  producer.flush()

def queue_job_detail_search(job_id: str, url: str):
  producer = KafkaProducer(bootstrap_servers=KAFKA_HOST)
  event = JobDetailEvent(job_id, url)
  producer.send(CRAWLER_TOPIC, value=event.get_event_value())
  producer.flush()