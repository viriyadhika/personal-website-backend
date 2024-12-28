from app.crawler.model.batch_relationship import (
    BatchRelationshipDto,
)
from app.crawler.model.base import BatchRelationship
from sqlalchemy.orm import Session
from app.db.engine import engine


def insert_batch_relationship(batch: BatchRelationshipDto):
    with Session(engine) as session:
        try:
            print(f"Inserting batch relationship {batch}")
            new_batch_relationship = BatchRelationship(
                batch_id=batch.batch_id, job_id=batch.job_id
            )
            session.add(new_batch_relationship)
            session.commit()
        except Exception as err:
            print(f"Fail inserting batch relationship {batch} {err}")
