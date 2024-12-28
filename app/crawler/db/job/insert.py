from app.crawler.model.job import JobDto
from app.db.engine import engine
from sqlalchemy.orm import Session
from sqlalchemy import select, or_, update
from app.crawler.model.base import Job


def insert_job(job: JobDto):
    with Session(engine) as session:
        print(f"Inserting job {job}")
        try:
            new_job = Job(
                job_id=job.id,
                name=job.title,
                link=job.link,
                description=job.description,
                company_id=job.company.id,
            )
            session.add(new_job)
            session.commit()
        except Exception as err:
            print(f"Error inserting {job} {err}")


def can_enhance_job(job_id: str):
    with Session(engine) as session:
        print(f"Checking job_id exist {job_id}")
        try:
            statement = (
                select(Job)
                .where(or_(Job.description.is_(None), Job.description == ""))
                .where(Job.job_id == job_id)
            )
            result = session.scalars(statement).one_or_none
            return result is not None
        except Exception as err:
            print(f"Error checking job {job_id} {err}")
            return False


def enrich_job(job: JobDto):
    with Session(engine) as session:
        print(f"Updating company {job}")
        try:
            statement = (
                update(Job)
                .where(Job.job_id == job.id)
                .values(description=job.description)
            )
            session.execute(statement)
            session.commit()
        except Exception as err:
            print(f"Error enriching {job} {err}")
