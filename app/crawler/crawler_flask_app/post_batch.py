from .middleware.validation_middleware import validate_payload
from app.crawler.crawler_module import main_producer
from .response import AppResponse, Result
from flask import abort, make_response

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
    main_producer.run(payload['keywords'], payload['location'])
    return AppResponse(Result.SUCCESS, data={}).get_response()
  except Exception as err:
    return abort(AppResponse(Result.ERROR, message=str(err)).get_response())