import mysql.connector
from app.env import MYSQL_PASSWORD, MYSQL_USER, MYSQL_DATABASE, MYSQL_HOST

class ConnectionWrapper():
  def __init__(self) -> None:
    self.connection = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD,
                              host=MYSQL_HOST,
                              database=MYSQL_DATABASE)
    self.cursor = self.connection.cursor()
    pass
  def __enter__(self):
    return self
  
  def __exit__(self, exception_type, exception_value, traceback):
    self.cursor.close()
    self.connection.close()

def get_cursor():
  return ConnectionWrapper()