from .middleware.validation_middleware import validate_payload

def handle_get_batch(payload):
  schema = {}

  validate_payload(payload, )
  pass