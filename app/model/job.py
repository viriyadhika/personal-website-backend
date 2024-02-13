from .company import Company
JOB_TABLE = 'job'

class JobColumn():
  id = 'id'
  job_id = 'job_posting_id'
  company = 'company'
  name = 'job_name'
  link = 'link'
  batch_id = 'batch'

class Job():
  def __init__(self, id: str, title: str, company: Company, link: str, batch_id: str) -> None:
    self.id = id
    self.title = title
    self.link = link
    self.company = company
    self.batch_id = batch_id

  def get_dictionary(self):
    dictionary = {
      JobColumn.job_id: self.id,
      JobColumn.name: self.title,
      JobColumn.link: self.link,
      JobColumn.company: self.company.id,
      JobColumn.batch_id: self.batch_id
    }
    return dictionary
  
  def __str__(self):
    dictionary = self.get_dictionary()
    return f'''
      {dictionary}
      company: {self.company}
    '''