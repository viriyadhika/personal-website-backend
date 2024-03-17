from app.crawler.model.batch_relationship import BatchRelationshipColumn, BatchRelationship, BATCH_RELATIONSHIP_TABLE
from ..connection import get_cursor

def insert_batch_relationship(batch: BatchRelationship):
  query = (
    f"INSERT INTO `{BATCH_RELATIONSHIP_TABLE}` "
    f"({BatchRelationshipColumn.batch_id}, {BatchRelationshipColumn.job_id}, {BatchRelationshipColumn.timestamp}) "
    f"VALUES (%({BatchRelationshipColumn.batch_id})s, %({BatchRelationshipColumn.job_id})s, curdate())"
  )

  with get_cursor() as wrapper:
    try:
      print(f'Inserting batch relationship {batch}')
      wrapper.cursor.execute(query, batch.get_dictionary())
      wrapper.connection.commit()
    except Exception as err:
      print(f'Fail inserting batch relationship {batch} {err}')

