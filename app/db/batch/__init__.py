from app.model.batch import BatchColumn, Batch, BATCH_TABLE
from ..connection import get_cursor

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
      print(f'Fail inserting batch {batch} {err}')

