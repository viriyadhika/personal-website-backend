from model.company import Company

class JobColumn():
  id = 'id'
  job_id = 'job_posting_id'
  company = 'company'
  name = 'job_name'
  link = 'link'
class Job():
  def __init__(self, id: str, title: str, company: Company, link: str) -> None:
    self.dictionary = {
      JobColumn.job_id: id,
      JobColumn.name: title,
      JobColumn.link: link
    }
    self.company = company

  def get_dictionary(self):
    dictionary = self.dictionary.copy()
    dictionary[JobColumn.company] = self.company.get_id()
    return dictionary
  
  def __str__(self):
    return f'''
      {self.dictionary}
      company: {self.company}
    '''