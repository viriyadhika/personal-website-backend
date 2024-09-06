from app.crawler.model.batch_relationship import (
    BatchRelationshipColumn,
    BATCH_RELATIONSHIP_TABLE,
)
from app.crawler.model.job import JobColumn, JOB_TABLE
from app.crawler.model.company import CompanyColumn, COMPANY_TABLE
from app.db.connection import get_cursor
from typing import List


class BatchContentResult:
    def __init__(
        self,
        company: str,
        job_id: str,
        job_name: str,
        link: str,
        description: str,
        employee: str,
    ) -> None:
        self.company = company
        self.job_id = job_id
        self.employee = employee
        self.job_name = job_name
        self.description = description
        self.link = link

    def get_dict(self):
        return {
            "company": self.company,
            "job_id": self.job_id,
            "job_name": self.job_name,
            "employee": self.employee,
            "link": self.link,
            "description": self.description,
        }


def get_batch_content(id, timestamp) -> List[BatchContentResult]:
    query = (
        f"SELECT {COMPANY_TABLE}.{CompanyColumn.name}, {JOB_TABLE}.{JobColumn.job_id}, {JOB_TABLE}.{JobColumn.name}, {JOB_TABLE}.{JobColumn.link}, {JOB_TABLE}.{JobColumn.description}, {COMPANY_TABLE}.{CompanyColumn.employee} "
        f"FROM {BATCH_RELATIONSHIP_TABLE} "
        f"LEFT JOIN {JOB_TABLE} "
        f"ON {BATCH_RELATIONSHIP_TABLE}.{BatchRelationshipColumn.job_id} = {JOB_TABLE}.{JobColumn.job_id} "
        f"LEFT JOIN {COMPANY_TABLE} "
        f"ON {COMPANY_TABLE}.{CompanyColumn.company_id} = {JOB_TABLE}.{JobColumn.company} "
        f"WHERE {BATCH_RELATIONSHIP_TABLE}.{BatchRelationshipColumn.batch_id} = %({BatchRelationshipColumn.batch_id})s AND "
        f"{BATCH_RELATIONSHIP_TABLE}.{BatchRelationshipColumn.timestamp} = %({BatchRelationshipColumn.timestamp})s "
        f"ORDER BY {COMPANY_TABLE}.{CompanyColumn.employee}, {COMPANY_TABLE}.{CompanyColumn.company_id}"
    )

    with get_cursor() as wrapper:
        try:
            wrapper.cursor.execute(
                query,
                {
                    BatchRelationshipColumn.batch_id: id,
                    BatchRelationshipColumn.timestamp: timestamp,
                },
            )
            result = []
            for (
                company,
                job_id,
                job_name,
                link,
                description,
                employee_number,
            ) in wrapper.cursor:
                result.append(
                    BatchContentResult(
                        company=company,
                        job_id=job_id,
                        job_name=job_name,
                        employee=employee_number,
                        link=link,
                        description=description,
                    )
                )
            return result
        except Exception as err:
            print(f"Fail querying batch relationship {id} {err}")
