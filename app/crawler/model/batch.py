
BATCH_TABLE = 'batch' 

class BatchColumn():
  id = 'id'
  batch_id = 'batch_id'
  last_updated = 'last_updated'

class Batch():
  def __init__(self, batch_id: str, last_updated: str) -> None:
    self.batch_id = batch_id
    self.last_updated = last_updated
  
  def get_dictionary(self):
    return {
      BatchColumn.batch_id: self.batch_id,
      BatchColumn.last_updated: self.last_updated
    }

  def __str__(self) -> str:
    dictionary = {
      BatchColumn.batch_id: self.batch_id,
    }
    return dictionary.__str__()