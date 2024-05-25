from enum import Enum
import json

class PipelineType(Enum):
  JOB = 'job'
  COMPANY = 'company'
  JOB_DETAIL = 'job_detail'

class EventKey():
  PIPELINE_TYPE = 'pipeline_type'
  PAYLOAD = 'payload'

class Event():
  # Create event class before sending event
  def __init__(self, pipeline_type: PipelineType, payload: dict) -> None:
    self.pipeline_type = pipeline_type
    self.payload = payload

  def get_event_value(self):
    return json.dumps({
      EventKey.PIPELINE_TYPE: self.pipeline_type.name,
      EventKey.PAYLOAD: self.payload
    }).encode('ASCII')
  
class JobEvent(Event):
  def __init__(self, location: str, keywords: str, batch_id: str):
    self.location = location
    self.keywords = keywords
    self.batch_id = batch_id
    super().__init__(PipelineType.JOB, { 'location': location, 'keywords': keywords, 'batch_id': batch_id })

class CompanyEvent(Event):
  def __init__(self, company_id: str, url: str):
    self.company_id = company_id
    self.url = url
    super().__init__(PipelineType.COMPANY, { 'company_id': company_id, 'url': url })

class JobDetailEvent(Event):
  def __init__(self, job_id: str, url: str):
    self.job_id = job_id
    self.url = url
    super().__init__(PipelineType.JOB_DETAIL, { 'job_id': job_id, 'url': url })

# Create Event class from received event
def create_event(event_message: dict):
  pipeline_type = event_message[EventKey.PIPELINE_TYPE]
  if (pipeline_type == PipelineType.JOB.name):
    payload = event_message[EventKey.PAYLOAD]
    return JobEvent(payload['location'], payload['keywords'], payload['batch_id'])
  if (pipeline_type == PipelineType.COMPANY.name):
    payload = event_message[EventKey.PAYLOAD]
    return CompanyEvent(payload['company_id'], payload['url'])
  if (pipeline_type == PipelineType.JOB_DETAIL.name):
    payload = event_message[EventKey.PAYLOAD]
    return JobDetailEvent(payload['job_id'], payload['url'])