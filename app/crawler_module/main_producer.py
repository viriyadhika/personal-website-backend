from .mq.producer import queue_job_search

def run():
  location = 'Singapore'
  keywords = 'Software Engineer'
  queue_job_search(location, keywords)

if __name__ == '__main__':
  run()