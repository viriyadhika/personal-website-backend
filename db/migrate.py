from db.connection import get_cursor
from mysql.connector import Error as ConnectorError, errorcode
from model.job import JobColumn
from model.company import CompanyColumn

TABLES = {}

TABLES['job'] = (
    f"CREATE TABLE `job` ("
    f"`{JobColumn.id}` int(11) NOT NULL AUTO_INCREMENT,"
    f"`{JobColumn.job_id}` varchar(25) UNIQUE NOT NULL,"
    f"`{JobColumn.name}` varchar(100) NOT NULL,"
    f"`{JobColumn.link}` varchar(300) NOT NULL,"
    f"PRIMARY KEY (`{JobColumn.id}`)"
    f") ENGINE=InnoDB"
)

TABLES['company'] = (
    f"CREATE TABLE `company` ("
    f"`{CompanyColumn.id}` int(11) NOT NULL AUTO_INCREMENT,"
    f"`{CompanyColumn.company_id}` varchar(25) UNIQUE NOT NULL,"
    f"`{CompanyColumn.name}` varchar(100) NOT NULL,"
    f"`{CompanyColumn.link}` varchar(300) NOT NULL,"
    f"PRIMARY KEY (`{CompanyColumn.id}`)"
    f") ENGINE=InnoDB"
)

def migrate():
  with get_cursor() as connection_wrapper:
    for table_name in TABLES:
      table_description = TABLES[table_name]
      try:
          print("Creating table {}: ".format(table_name), end='')
          connection_wrapper.cursor.execute(table_description)
      except ConnectorError as err:
          if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
              print("already exists.")
          else:
              print(err.msg)
      else:
          print("OK")

