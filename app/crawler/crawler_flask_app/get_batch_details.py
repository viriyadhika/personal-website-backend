from app.crawler.db.batch_company import get_batch_content
from .middleware.validation_middleware import validate_payload
from datetime import datetime

def get_db_result(id: str, timestamp: int):
  timestampStr = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
  return get_batch_content(id, timestampStr)


def handle_get_batch_details(request):
  schema = {
    "type" : "object",
    "properties" : {
        "id" : {"type" : "string"},
        "timestamp": { "type": "number" },
        "comparison_timestamp": { "type": "number" }
    },
    "required": ["id", "timestamp", "comparison_timestamp"]
  }
  validate_payload(request, schema)

  s = set()
  for i in get_db_result(request['id'], request['comparison_timestamp']):
    s.add(i.job_id)

  final_result = []
  for i in get_db_result(request['id'], request['timestamp']):
    final_result.append({ **i.get_dict(), 'is_new': i.job_id not in s })

  return final_result