from ..connection import get_cursor
from model.company import Company, CompanyColumn

def insert_company(company: Company):
  query = (
    f"INSERT INTO `company` "
    f"({CompanyColumn.company_id}, {CompanyColumn.name}, {CompanyColumn.link}) "
    f"VALUES (%({CompanyColumn.company_id})s, %({CompanyColumn.name})s, %({CompanyColumn.link})s)"
  )
  with get_cursor() as wrapper:
    print(f'Inserting company {company}')
    try:
      wrapper.cursor.execute(query, company.get_dictionary())
      wrapper.connection.commit()
    except Exception as err:
      print(f'Error inserting {company} {err}')
    

def enrich_company(company: Company):
  query = (
    f"UPDATE `company` "
    f"SET {CompanyColumn.employee} = %({CompanyColumn.employee})s "
    f"WHERE {CompanyColumn.company_id} = %({CompanyColumn.company_id})s"
  )
  with get_cursor() as wrapper:
    print(f'Updating company {company}')
    try:
      wrapper.cursor.execute(query, company.get_dictionary())
      wrapper.connection.commit()
    except Exception as err:
      print(f'Error enriching {company} {err}')