from app.db.connection import get_cursor
from mysql.connector import Error as ConnectorError, errorcode
from app.model.job import JobColumn, JOB_TABLE
from app.model.company import CompanyColumn, COMPANY_TABLE
from app.model.batch_relationship import BatchRelationshipColumn, BATCH_RELATIONSHIP_TABLE

TABLES = {}

TABLES[JOB_TABLE] = (
    f"CREATE TABLE `{JOB_TABLE}` ("
    f"`{JobColumn.id}` int(11) NOT NULL AUTO_INCREMENT,"
    f"`{JobColumn.job_id}` varchar(25) UNIQUE NOT NULL,"
    f"`{JobColumn.name}` varchar(100) NOT NULL,"
    f"`{JobColumn.link}` varchar(300) NOT NULL,"
    f"`{JobColumn.company}` varchar(25) NOT NULL,"
    f"PRIMARY KEY (`{JobColumn.id}`), "
    f"FOREIGN KEY ({JobColumn.company}) REFERENCES company({CompanyColumn.company_id}) ON DELETE CASCADE"
    f") ENGINE=InnoDB"
)

TABLES[COMPANY_TABLE] = (
    f"CREATE TABLE `{COMPANY_TABLE}` ("
    f"`{CompanyColumn.id}` int(11) NOT NULL AUTO_INCREMENT,"
    f"`{CompanyColumn.company_id}` varchar(25) UNIQUE NOT NULL,"
    f"`{CompanyColumn.name}` varchar(100) NOT NULL,"
    f"`{CompanyColumn.link}` varchar(300),"
    f"`{CompanyColumn.employee}` varchar(25),"
    f"PRIMARY KEY (`{CompanyColumn.id}`)"
    f") ENGINE=InnoDB"
)

TABLES[BATCH_RELATIONSHIP_TABLE] = (
    f"CREATE TABLE `{BATCH_RELATIONSHIP_TABLE}` ("
    f"`{BatchRelationshipColumn.id}` int(11) NOT NULL AUTO_INCREMENT,"
    f"`{BatchRelationshipColumn.batch_id}` varchar(100) NOT NULL,"
    f"`{BatchRelationshipColumn.job_id}` varchar(25) NOT NULL,"
    f""
    f"PRIMARY KEY (`{BatchRelationshipColumn.id}`), "
    f"FOREIGN KEY ({BatchRelationshipColumn.job_id}) REFERENCES job({JobColumn.job_id}) ON DELETE CASCADE"
    f") ENGINE=InnoDB"
)

EXTRA = [
    {
        'name': 'Create batch relationship unique index',
        'script': (
          f"ALTER TABLE `{BATCH_RELATIONSHIP_TABLE}` "
          f"ADD UNIQUE `unique_index` (`{BatchRelationshipColumn.batch_id}`, `{BatchRelationshipColumn.job_id}`);"
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