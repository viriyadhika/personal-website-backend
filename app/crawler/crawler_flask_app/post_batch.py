from .middleware.validation_middleware import validate_payload
from app.crawler.crawler_module import main_producer
from .response import AppResponse, Result
from flask import abort

def handle_post_batch(payload):
  schema = {
    "type" : "object",
    "properties" : {
        "keywords" : {"type" : "string"},
        "location" : {"type" : "string"},
    },
    "required": ["keywords", "location"]
  }
  validate_payload(payload, schema)
  try:
    main_producer.run(payload['location'], payload['keywords'])
    return AppResponse(Result.SUCCESS, data={}).get_response()
  except Exception as err:
    return abort(AppResponse(Result.ERROR, message=str(err)).get_response())