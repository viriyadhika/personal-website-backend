from app.crawler.model.batch import BatchColumn, Batch, Status, BATCH_TABLE
from ..connection import get_cursor
from typing import List

def insert_batch(batch: Batch):
  query = (
    f"INSERT INTO `{BATCH_TABLE}` "
    f"({BatchColumn.batch_id}, {BatchColumn.status}) "
    f"VALUES (%({BatchColumn.batch_id})s, %({BatchColumn.status})s)"
  )

  with get_cursor() as wrapper:
    try:
      print(f'Inserting batch {batch}')
      wrapper.cursor.execute(query, batch.get_dictionary())
      wrapper.connection.commit()
    except Exception as err:
      raise Exception(f'Fail inserting batch {batch} {err}')

def get_all_batch() -> List[Batch]:
  query = (
    f"SELECT {BatchColumn.batch_id}, {BatchColumn.status} "
    f"FROM {BATCH_TABLE}"
  )

  with get_cursor() as wrapper:
    try:
      print(f'Getting all batch')
      wrapper.cursor.execute(query)
      for (batch_id, status) in wrapper.cursor:
        result = []
        result.append(Batch(batch_id, Status(status)))
      return result
    except Exception as err:
      raise Exception(f'Fail querying batch')