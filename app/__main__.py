import argparse

from app.crawler.crawler_module import main_consumer
from app.crawler.crawler_module import main_producer

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Run task", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument('command', help='Either "producer" or "consumer"')
  argument = vars(parser.parse_args())
  

  command = argument['command']
  if (command == 'producer'):
    main_producer.run('Singapore', 'Software Engineer')
  if (command == 'consumer'):
    main_consumer.run()