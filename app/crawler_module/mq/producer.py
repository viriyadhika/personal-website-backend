from kafka import KafkaProducer
from app.env import crawler_topic
from app.crawler_module.mq.event_model import JobEvent, CompanyEvent
from app.crawler_module.utils.utils import generate_batch_id

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def queue_job_search(location: str, keywords: str):
  event = JobEvent(location, keywords, generate_batch_id(location, keywords))
  producer.send(crawler_topic, value=event.get_event_value())
  producer.flush()

def queue_company_search(company_id: str, url: str):
  event = CompanyEvent(company_id, url)
  producer.send(crawler_topic, value=event.get_event_value())
  producer.flush()