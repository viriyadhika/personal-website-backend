from kafka import KafkaProducer
from env import crawler_topic
from .event_model import JobEvent, CompanyEvent

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def queue_job_search():
  event = JobEvent('Singapore', 'Software Engineer')
  producer.send(crawler_topic, value=event.get_event_value())
  producer.flush()

def queue_company_search(company_id: str, url: str):
  event = CompanyEvent(company_id, url)
  producer.send(crawler_topic, value=event.get_event_value())
  producer.flush()