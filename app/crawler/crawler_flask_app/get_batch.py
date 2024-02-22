from .middleware.validation_middleware import validate_payload
from app.crawler.db.batch import get_all_batch

def handle_get_batch():
  result = get_all_batch()
  response = []
  for i in result:
    response.append(i.get_dictionary())

  return response