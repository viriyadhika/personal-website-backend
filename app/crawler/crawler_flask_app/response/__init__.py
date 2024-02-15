from enum import Enum
from flask import make_response

class Result(Enum):
  SUCCESS = 'success'
  INVALID_PARAM = 'invalid param'
  ERROR = 'error'

class AppResponse():
  def __init__(self, result: Result, data=None, message=None):
    self.result = result
    self.data = data
    self.message = message

  def get_response(self):
    if (self.result == Result.SUCCESS):
      return make_response({
        'result': self.result.value,
        'data': self.data,
      }, 200)
    if (self.result == Result.INVALID_PARAM):
      return make_response({
        'result': self.result.value,
        'message': self.message,
      }, 400)
    if (self.result == Result.ERROR):
      return make_response({
        'result': self.result.value,
        'message': self.message,
      }, 500)
    return make_response({ 'result': Result.ERROR.value, 'message': 'Unknown error' }, 500)