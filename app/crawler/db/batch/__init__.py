from app.crawler.model.batch import BatchDto
from app.db.engine import engine
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import select, update
from app.crawler.model.base import Batch
from datetime import datetime


def insert_or_update_batch(batch: BatchDto):
    with Session(engine) as session:
        try:
            print(f"Inserting batch {batch}")
            statement = select(Batch).where(Batch.batch_id == batch.batch_id)
            existing_batch = session.scalars(statement).one_or_none()
            if existing_batch is not None:
                update_statement = (
                    update(Batch)
                    .where(Batch.batch_id == batch.batch_id)
                    .values(last_updated=datetime.now())
                )
                session.execute(update_statement)
            else:
                new_batch = Batch(
                    batch_id=batch.batch_id,
                    location=batch.location,
                    keywords=batch.keywords,
                )
                session.add(new_batch)

            session.commit()
        except Exception as err:
            print(f"Fail inserting batch {batch} {err}")


def get_all_batch() -> List[BatchDto]:
    with Session(engine) as session:
        try:
            print(f"Getting all batch")
            statement = select(Batch)
            batches = session.scalars(statement).fetchall()
            result = list(
                map(
                    lambda b: BatchDto(
                        batch_id=b.batch_id,
                        location=b.location,
                        keywords=b.keywords,
                        last_updated=b.last_updated,
                    ),
                    batches,
                )
            )
            return result
        except Exception as err:
            raise Exception(f"Fail querying batch")
