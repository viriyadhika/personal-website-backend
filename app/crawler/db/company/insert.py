from app.crawler.model.company import CompanyDto
from app.crawler.model.base import Company
from app.db.engine import engine
from sqlalchemy.orm import Session
from sqlalchemy import update, select


def insert_company(company: CompanyDto):
    with Session(engine) as session:
        print(f"Inserting company {company}")
        try:
            new_company = Company(
                company_id=company.id, name=company.name, link=company.link
            )
            session.add(new_company)
            session.commit()
        except Exception as err:
            print(f"Error inserting {company} {err}")


def enrich_company(company: CompanyDto):
    with Session(engine) as session:
        print(f"Updating company {company}")
        try:
            statement = (
                update(Company)
                .where(Company.company_id == company.id)
                .values(employee=company.employee)
            )
            session.execute(statement)
            session.commit()
        except Exception as err:
            print(f"Error enriching {company} {err}")


def check_company_exist(company_id: str):
    with Session(engine) as session:
        print(f"Finding company ID {company_id}")
        try:
            statement = select(Company.employee).where(Company.company_id == company_id)
            employee = session.scalars(statement).one_or_none()
            print(f"Company employee is {employee}")
            return (employee is not None) and (employee != "")
        except Exception as err:
            print(f"Error finding company {company_id} {err}")
