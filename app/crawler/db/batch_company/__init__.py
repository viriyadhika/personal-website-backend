from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.engine import engine
from app.crawler.model.base import BatchRelationship, Company, Job


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
    with Session(engine) as session:
        try:
            statement = (
                select(
                    Company.name,
                    Job.job_id,
                    Job.name,
                    Job.link,
                    Job.description,
                    Company.employee,
                )
                .join_from(BatchRelationship, Job)
                .join(Company)
                .where(BatchRelationship.batch_id == id)
                .where(BatchRelationship.timestamp == timestamp)
                .order_by(Company.employee, Company.company_id)
            )
            query_result = session.execute(statement).fetchall()
            result = []
            for (
                company,
                job_id,
                job_name,
                link,
                description,
                employee_number,
            ) in query_result:
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
            raise
