from enum import Enum

BATCH_TABLE = 'batch' 

class BatchColumn():
  id = 'id'
  batch_id = 'batch_id'
  status = 'status'

class Status(Enum):
  QUEUING = 1
  BATCH_RUNNING = 2
  COMPLETED = 3

class Batch():
  def __init__(self, batch_id: str, status: Status) -> None:
    self.batch_id = batch_id
    self.status = status
  
  def get_dictionary(self):
    return {
      BatchColumn.batch_id: self.batch_id,
      BatchColumn.status: int(self.status.value)
    }

  def __str__(self) -> str:
    dictionary = {
      BatchColumn.batch_id: self.batch_id,
      BatchColumn.status: self.status.name
    }
    return dictionary.__str__()