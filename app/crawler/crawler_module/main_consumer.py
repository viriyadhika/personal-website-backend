import threading
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


class MainConsumer:
    def __init__(self):
        self.consumer = get_consumer()
        self.stop_event = threading.Event()

    def close(self):
        self.stop_event.set()
        self.consumer.close()

    def run(self):
        while not self.stop_event.is_set():
            msg = self.consumer.poll(600)
            if msg is None or len(msg) == 0:
                continue

            for message_compartments in msg.values():
                for msg in message_compartments:
                    event = create_event(json.loads(msg.value.decode("ascii")))
                    if isinstance(event, JobEvent):
                        handle_job_consumer(event)
                    elif isinstance(event, CompanyEvent):
                        handle_company_consumer(event)
                    elif isinstance(event, JobDetailEvent):
                        handle_job_detail_consumer(event)
