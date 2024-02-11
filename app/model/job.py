from .company import Company

class JobColumn():
  id = 'id'
  job_id = 'job_posting_id'
  company = 'company'
  name = 'job_name'
  link = 'link'
class Job():
  def __init__(self, id: str, title: str, company: Company, link: str) -> None:
    self.id = id
    self.title = title
    self.link = link
    self.company = company

  def get_dictionary(self):
    dictionary = {
      JobColumn.job_id: self.id,
      JobColumn.name: self.title,
      JobColumn.link: self.link
    }
    dictionary[JobColumn.company] = self.company.id
    return dictionary
  
  def __str__(self):
    dictionary = self.get_dictionary()
    return f'''
      {dictionary}
      company: {self.company}
    '''