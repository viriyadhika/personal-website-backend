from app.db.connection import get_cursor
from app.crawler.model.job import JobColumn, Job, JOB_TABLE


def insert_job(job: Job):
    query = (
        f"INSERT INTO `{JOB_TABLE}` "
        f"({JobColumn.job_id}, {JobColumn.name}, {JobColumn.link}, {JobColumn.company}, {JobColumn.description}) "
        f"VALUES (%({JobColumn.job_id})s, %({JobColumn.name})s, %({JobColumn.link})s, %({JobColumn.company})s, %({JobColumn.description})s)"
    )
    with get_cursor() as wrapper:
        print(f"Inserting job {job}")
        try:
            wrapper.cursor.execute(query, job.get_dictionary())
            wrapper.connection.commit()
        except Exception as err:
            print(f"Error inserting {job} {err}")


def can_enhance_job(job_id: str):
    query = (
        f"SELECT COUNT({JobColumn.job_id}) FROM {JOB_TABLE} "
        f"WHERE ({JobColumn.description} IS NULL OR {JobColumn.description} = '') AND {JobColumn.job_id} = %({JobColumn.job_id})s"
    )
    with get_cursor() as wrapper:
        print(f"Checking job_id exist {job_id}")
        try:
            wrapper.cursor.execute(query, {JobColumn.job_id: job_id})
            for _ in wrapper.cursor:
                return True
            return False
        except Exception as err:
            print(f"Error checking job {job_id} {err}")
            return False


def enrich_job(job: Job):
    query = (
        f"UPDATE `{JOB_TABLE}` "
        f"SET {JobColumn.description} = %({JobColumn.description})s "
        f"WHERE {JobColumn.job_id} = %({JobColumn.job_id})s"
    )
    with get_cursor() as wrapper:
        print(f"Updating company {job}")
        try:
            wrapper.cursor.execute(query, job.get_dictionary())
            wrapper.connection.commit()
        except Exception as err:
            print(f"Error enriching {job} {err}")
