from app.crawler.model.batch_relationship import BatchRelationshipColumn, BATCH_RELATIONSHIP_TABLE
from app.crawler.model.job import JobColumn, JOB_TABLE
from app.crawler.model.company import CompanyColumn, COMPANY_TABLE
from ..connection import get_cursor

def get_batch_content(id):
  query = (
    f"SELECT {COMPANY_TABLE}.{CompanyColumn.name}, {JOB_TABLE}.{JobColumn.name}, {COMPANY_TABLE}.{CompanyColumn.employee} " 
    f"FROM {BATCH_RELATIONSHIP_TABLE} "
    f"LEFT JOIN {JOB_TABLE} "
    f"ON {BATCH_RELATIONSHIP_TABLE}.{BatchRelationshipColumn.job_id} = {JOB_TABLE}.{JobColumn.job_id} "
    f"LEFT JOIN {COMPANY_TABLE} "
    f"ON {COMPANY_TABLE}.{CompanyColumn.company_id} = {JOB_TABLE}.{JobColumn.company} "
    f"WHERE {BATCH_RELATIONSHIP_TABLE}.{BatchRelationshipColumn.batch_id} = %({BatchRelationshipColumn.batch_id})s "
  )

  with get_cursor() as wrapper:
    try:
      wrapper.cursor.execute(query, { BatchRelationshipColumn.batch_id: id })
      result = []
      for (company, job_id, employee_number) in wrapper.cursor:
        result.append({ 'company': company, 'job_id': job_id, 'employee': employee_number })
      return result
    except Exception as err:
      print(f'Fail querying batch relationship {id} {err}')