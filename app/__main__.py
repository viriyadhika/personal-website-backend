import argparse

from app.crawler.crawler_module import main_consumer
from app.crawler.crawler_module import main_producer
from app.crawler.db.migrate import migrate
from app.auth.db import init_auth_db
from app.crawler.crawler_module import create_topic

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Run task", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument('command', help='Either "producer", "consumer" or "setup"')
  argument = vars(parser.parse_args())
  
  print(f'Running command with {argument}')

  try:
    command = argument['command']
    if (command == 'producer'):
      main_producer.run('Singapore', 'Software Engineer')
    if (command == 'consumer'):
      main_consumer.run()
    if (command == 'setup'):
      migrate()
      init_auth_db()
      create_topic.run()
  except KeyboardInterrupt:
    pass