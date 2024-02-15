
from jsonschema import validate, ValidationError
from flask import abort, make_response, Response
from ..response import AppResponse, Result

def validate_payload(payload, schema):
  try:
    validate(instance=payload, schema=schema)
  except ValidationError as err:
    abort(AppResponse(Result.INVALID_PARAM, message=err.message).get_response())
  except Exception as err:
    return abort(AppResponse(Result.ERROR, message=str(err)).get_response())