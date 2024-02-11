
class Company():
  def __init__(self, id, name, link) -> None:
    self.id = id
    self.name = name
    self.link = link
  
  def __str__(self) -> str:
    return f'''
      id: {self.id}
      name: {self.name}
      link: {self.link}
    '''