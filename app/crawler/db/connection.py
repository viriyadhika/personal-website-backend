import mysql.connector
from app.env import DB_PASSWORD, DB_USERNAME

class ConnectionWrapper():
  def __init__(self) -> None:
    self.connection = mysql.connector.connect(user=DB_USERNAME, password=DB_PASSWORD,
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