from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError
from app.env import KAFKA_HOST, CRAWLER_TOPIC

def create(admin_client: KafkaAdminClient, topic_name: str):
  # Create a NewTopic instance
  try:
    new_topic = NewTopic(
        name=topic_name,
        num_partitions=1,
        replication_factor=1
    )
    # Create the topic
    admin_client.create_topics([new_topic])
    print(f"Topic '{topic_name}' created successfully.")
  except TopicAlreadyExistsError as err:
    print(err) 

def run():
  # Create an AdminClient instance
  admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_HOST, client_id='topic_creator')
  topic_name = CRAWLER_TOPIC
  create(admin_client, topic_name)