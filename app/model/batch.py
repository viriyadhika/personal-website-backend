
class BatchColumn():
  id = 'id'
  batch_id = 'BATCH_ID'
  job_id = 'JOB_ID'

class Batch():
  def __init__(self, batch_id: str, job_id: str) -> None:
    self.batch_id = batch_id
    self.job_id = job_id
  
  def get_dictionary(self):
    return {
      BatchColumn.batch_id: self.batch_id,
      BatchColumn.job_id: self.job_id
    }

  def __str__(self) -> str:
    dictionary = self.get_dictionary()
    return dictionary.__str__()