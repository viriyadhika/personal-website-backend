import mysql.connector
from app.crawler.env import db_password, db_username

class ConnectionWrapper():
  def __init__(self) -> None:
    self.connection = mysql.connector.connect(user=db_username, password=db_password,
                              host='127.0.0.1',
                              database='crawler')
    self.cursor = self.connection.cursor()
    pass
  def __enter__(self):
    return self
  
  def __exit__(self, exception_type, exception_value, traceback):
    self.cursor.close()
    self.connection.close()

def get_cursor():
  return ConnectionWrapper()