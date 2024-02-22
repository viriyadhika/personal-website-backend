from app.crawler.db.batch_company import get_batch_content
from .middleware.validation_middleware import validate_payload

def handle_get_batch_details(request):
  schema = {
    "type" : "object",
    "properties" : {
        "id" : {"type" : "string"}
    },
    "required": ["id"]
  }
  validate_payload(request, schema)
  return get_batch_content(request['id'])