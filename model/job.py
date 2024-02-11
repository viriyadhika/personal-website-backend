from model.company import Company

class Job():
  def __init__(self, id: str, title: str, company: Company, link: str) -> None:
    self.title = title
    self.company = company
    self.id = id
    self.link = link
  
  def __str__(self):
    return f'''
      id: {self.id}
      title: {self.title}
      link: {self.link}
      company: {self.company}
    '''