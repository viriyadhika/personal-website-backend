import time
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable
from app.env import CRAWLER_TOPIC, KAFKA_HOST
import json
from app.crawler.crawler_module.mq.event_model import (
    JobDetailEvent,
    create_event,
    JobEvent,
    CompanyEvent,
)
from app.crawler.crawler_module.controller.job import handle_job_consumer
from app.crawler.crawler_module.controller.company import handle_company_consumer
from app.crawler.crawler_module.controller.job_detail import handle_job_detail_consumer


def get_consumer():
    retries = 0
    while retries < 10:
        try:
            consumer = KafkaConsumer(CRAWLER_TOPIC, bootstrap_servers=KAFKA_HOST)
            return consumer
        except NoBrokersAvailable:
            print(
                f"No brokers available. Retrying in 5 seconds... (Attempt {retries + 1}/10)"
            )
            time.sleep(5)
            retries += 1
        except Exception as e:
            print(f"An error occurred: {e}")
            raise e


def run():
    consumer = get_consumer()
    for message in consumer:
        event = create_event(json.loads(message.value))
        if isinstance(event, JobEvent):
            handle_job_consumer(event)
        if isinstance(event, CompanyEvent):
            handle_company_consumer(event)
        if isinstance(event, JobDetailEvent):
            handle_job_detail_consumer(event)
