from app.crawler.model.batch import BatchColumn, Batch, BATCH_TABLE
from ..connection import get_cursor
from typing import List
from mysql.connector import IntegrityError

def insert_or_update_batch(batch: Batch):
  query = (
    f"INSERT INTO `{BATCH_TABLE}` "
    f"({BatchColumn.batch_id}, {BatchColumn.last_updated}) "
    f"VALUES (%({BatchColumn.batch_id})s, curdate())"
  )

  update_query = (
    f"UPDATE `{BATCH_TABLE}` "
    f"SET {BatchColumn.last_updated} =  curdate() "
    f"WHERE {BatchColumn.batch_id} = %({BatchColumn.batch_id})s"
  )

  with get_cursor() as wrapper:
    try:
      print(f'Inserting batch {batch}')
      wrapper.cursor.execute(query, batch.get_dictionary())
      wrapper.connection.commit()
    except IntegrityError as err:

      try:
        print(f'Integrity error, updating {batch}')
        wrapper.cursor.execute(update_query, batch.get_dictionary())
        wrapper.connection.commit()
      except Exception as err:
        print(f'Fail updating batch {batch} {err}')

    except Exception as err:
      print(f'Fail inserting batch {batch} {err}')

def get_all_batch() -> List[Batch]:
  query = (
    f"SELECT {BatchColumn.batch_id}, {BatchColumn.last_updated} "
    f"FROM {BATCH_TABLE}"
  )

  with get_cursor() as wrapper:
    try:
      print(f'Getting all batch')
      wrapper.cursor.execute(query)
      result = []
      for (batch_id, last_updated) in wrapper.cursor:
        result.append(Batch(batch_id, last_updated))
      return result
    except Exception as err:
      raise Exception(f'Fail querying batch')