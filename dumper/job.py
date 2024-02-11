from db.connection import get_cursor


def dump_data():
  # cnx = mysql.connector.connect(user='viriyadhika', password='Blahello!123',
  #                             host='127.0.0.1',
  #                             database='crawler')
  
  with get_cursor() as wrapper:
    dump_job = 'INSERT INTO '


