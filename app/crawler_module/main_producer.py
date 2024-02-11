from .mq.producer import queue_job_search

def run():
  queue_job_search()

if __name__ == '__main__':
  run()