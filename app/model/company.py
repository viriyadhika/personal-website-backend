
class CompanyColumn():
  id = 'id'
  company_id = 'company_id'
  name = 'company_name'
  link = 'link'
  employee = 'employee'


class Company():
  def __init__(self, company_id: str, name: str = '', link: str = '', employee: str = '') -> None:
    self.id = company_id
    self.name = name
    self.link = link
    self.employee = employee

  def get_dictionary(self):
    return {
      CompanyColumn.company_id: self.id,
      CompanyColumn.name: self.name,
      CompanyColumn.link: self.link,
      CompanyColumn.employee: self.employee
    }

  def __str__(self) -> str:
    obj = self.get_dictionary()
    return obj.__str__()