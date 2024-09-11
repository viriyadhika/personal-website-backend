from dataclasses import dataclass
from typing import List
from app.db.connection import get_cursor
from mysql.connector import Error as ConnectorError, errorcode


@dataclass()
class ExtraScript:
    name: str
    script: str


def migrate(TABLES: dict[str, str], EXTRA: List[ExtraScript]):
    with get_cursor() as connection_wrapper:
        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print("Creating table {}: ".format(table_name), end="")
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
                print(extra_script.name)
                connection_wrapper.cursor.execute(extra_script.script)
            except ConnectorError as err:
                print(err.msg)
            else:
                print("OK")
