from app.db.connection import get_cursor
from mysql.connector import Error as ConnectorError, errorcode
from app.model.job import JobColumn
from app.model.company import CompanyColumn
from app.model.batch import BatchColumn

TABLES = {}

TABLES['job'] = (
    f"CREATE TABLE `job` ("
    f"`{JobColumn.id}` int(11) NOT NULL AUTO_INCREMENT,"
    f"`{JobColumn.job_id}` varchar(25) UNIQUE NOT NULL,"
    f"`{JobColumn.name}` varchar(100) NOT NULL,"
    f"`{JobColumn.link}` varchar(300) NOT NULL,"
    f"`{JobColumn.company}` varchar(25) NOT NULL,"
    f"PRIMARY KEY (`{JobColumn.id}`), "
    f"FOREIGN KEY ({JobColumn.company}) REFERENCES company({CompanyColumn.company_id}) ON DELETE CASCADE"
    f") ENGINE=InnoDB"
)

TABLES['company'] = (
    f"CREATE TABLE `company` ("
    f"`{CompanyColumn.id}` int(11) NOT NULL AUTO_INCREMENT,"
    f"`{CompanyColumn.company_id}` varchar(25) UNIQUE NOT NULL,"
    f"`{CompanyColumn.name}` varchar(100) NOT NULL,"
    f"`{CompanyColumn.link}` varchar(300),"
    f"`{CompanyColumn.employee}` varchar(25),"
    f"PRIMARY KEY (`{CompanyColumn.id}`)"
    f") ENGINE=InnoDB"
)

TABLES['batch'] = (
    f"CREATE TABLE `batch` ("
    f"`{BatchColumn.id}` int(11) NOT NULL AUTO_INCREMENT,"
    f"`{BatchColumn.batch_id}` varchar(100) NOT NULL,"
    f"`{BatchColumn.job_id}` varchar(25) NOT NULL,"
    f""
    f"PRIMARY KEY (`{BatchColumn.id}`), "
    f"FOREIGN KEY ({BatchColumn.job_id}) REFERENCES job({JobColumn.job_id}) ON DELETE CASCADE"
    f") ENGINE=InnoDB"
)

EXTRA = [
    {
        'name': 'Create batch unique index',
        'script': (
          f"ALTER TABLE `batch` "
          f"ADD UNIQUE `unique_index` (`{BatchColumn.batch_id}`, `{BatchColumn.job_id}`);"
        )
   }
]

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

    for extra_script in EXTRA:
        try:
            print(extra_script['name'])
            connection_wrapper.cursor.execute(extra_script['script'])
        except ConnectorError as err:
            print(err.msg)
        else:
            print("OK")