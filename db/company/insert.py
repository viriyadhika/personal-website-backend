from db.connection import get_cursor
from model.company import Company, CompanyColumn

query = (
    f"INSERT INTO `company` "
    f"({CompanyColumn.company_id}, {CompanyColumn.name}, {CompanyColumn.link}) "
    f"VALUES (%({CompanyColumn.company_id})s, %({CompanyColumn.name})s, %({CompanyColumn.link})s)"
)

def insert_company(company: Company):
  with get_cursor() as wrapper:
    print('Inserting company {company}')
    try:
      wrapper.cursor.execute(query, company.get_dictionary())
      wrapper.connection.commit()
    except Exception as err:
      print(f'Error inserting {company} {err}')
    

