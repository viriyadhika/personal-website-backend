from kafka import KafkaConsumer
from app.crawler.env import crawler_topic
import json
from app.crawler.crawler_module.mq.event_model import create_event, JobEvent, CompanyEvent
from app.crawler.db.migrate import migrate
from app.crawler.crawler_module.controller.job import handle_job_consumer
from app.crawler.crawler_module.controller.company import handle_company_consumer

consumer = KafkaConsumer(crawler_topic)

def run():
  migrate()
  for message in consumer:
    event = create_event(json.loads(message.value))
    if (isinstance(event, JobEvent)):
      handle_job_consumer(event)

    if (isinstance(event, CompanyEvent)):
      handle_company_consumer(event)

if __name__ == '__main__':
  run()
