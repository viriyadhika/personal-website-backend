from app.crawler.model.job import JobDto
from app.db.engine import engine
from sqlalchemy.orm import Session
from sqlalchemy import select, or_, update
from app.crawler.model.base import VPTime


def query_ptime(ctry: str):
    with Session(engine) as session:
        try:
            statement = select(VPTime).where(VPTime.ctry_code == ctry)
            ptimes = session.scalars(statement).fetchall()

            return ptimes
        except Exception as err:
            print(f"Error querying {err}")


def insert_ptime(v_ptimes: list[VPTime]):
    with Session(engine) as session:
        print(f"Inserting ptime {[v_ptime.__dict__ for v_ptime in v_ptimes ]}")
        try:
            session.add_all(v_ptimes)
            session.commit()
        except Exception as err:
            print(f"Error inserting ptime {v_ptimes} {err}")
