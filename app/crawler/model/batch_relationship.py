BATCH_RELATIONSHIP_TABLE = 'batch_relationship' 

class BatchRelationshipColumn():
  id = 'id'
  batch_id = 'batch_id'
  job_id = 'job_id'
  timestamp = 'timestamp'

class BatchRelationship():
  def __init__(self, batch_id: str, job_id: str) -> None:
    self.batch_id = batch_id
    self.job_id = job_id
  
  def get_dictionary(self):
    return {
      BatchRelationshipColumn.batch_id: self.batch_id,
      BatchRelationshipColumn.job_id: self.job_id
    }

  def __str__(self) -> str:
    dictionary = self.get_dictionary()
    return dictionary.__str__()