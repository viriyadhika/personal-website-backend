from kafka import KafkaConsumer
from app.env import CRAWLER_TOPIC, KAFKA_HOST
import json
from app.crawler.crawler_module.mq.event_model import create_event, JobEvent, CompanyEvent
from app.crawler.crawler_module.controller.job import handle_job_consumer
from app.crawler.crawler_module.controller.company import handle_company_consumer

def run():
  consumer = KafkaConsumer(CRAWLER_TOPIC, bootstrap_servers=KAFKA_HOST)
  for message in consumer:
    event = create_event(json.loads(message.value))
    if (isinstance(event, JobEvent)):
      handle_job_consumer(event)

    if (isinstance(event, CompanyEvent)):
      handle_company_consumer(event)
