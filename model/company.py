
class CompanyColumn():
  id = 'id'
  company_id = 'company_id'
  name = 'company_name'
  link = 'link'


class Company():
  def __init__(self, id: str, name: str, link: str) -> None:
    self.obj = {
      CompanyColumn.company_id: id,
      CompanyColumn.name: name,
      CompanyColumn.link: link
    }

  def get_id(self):
    return self.obj[CompanyColumn.company_id]

  def get_link(self):
    return self.obj[CompanyColumn.link]
  
  def get_dictionary(self):
    return self.obj

  def __str__(self) -> str:
    return self.obj.__str__()