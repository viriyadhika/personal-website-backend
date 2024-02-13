from ..connection import get_cursor
from app.model.job import JobColumn, Job, JOB_TABLE

query = (
    f"INSERT INTO `{JOB_TABLE}` "
    f"({JobColumn.job_id}, {JobColumn.name}, {JobColumn.link}, {JobColumn.company}) "
    f"VALUES (%({JobColumn.job_id})s, %({JobColumn.name})s, %({JobColumn.link})s, %({JobColumn.company})s)"
)

def insert_job(job: Job):
  with get_cursor() as wrapper:
    print(f'Inserting job {job}')
    try:
      wrapper.cursor.execute(query, job.get_dictionary())
      wrapper.connection.commit()
    except Exception as err:
      print(f'Error inserting {job} {err}')
    

