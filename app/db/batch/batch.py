from model.batch import BatchColumn, Batch
from ..connection import get_cursor

def insert_batch(batch: Batch):
  query = (
    f"INSERT INTO `batch` "
    f"({BatchColumn.batch_id}, {BatchColumn.job_id}) "
    f"VALUES (%({BatchColumn.batch_id})s, %({BatchColumn.job_id})s)"
  )

  with get_cursor() as wrapper:
    try:
      print(f'Inserting batch {batch}')
      wrapper.cursor.execute(query, batch.get_dictionary())
      wrapper.connection.commit()
    except Exception as err:
      print(f'Fail inserting batch {batch} {err}')

