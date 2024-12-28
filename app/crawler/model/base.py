from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, ForeignKey, DateTime, UniqueConstraint, Date
from sqlalchemy.orm import mapped_column, Mapped, relationship
import datetime
from typing import List
from sqlalchemy.sql import func


class CrawlerBase(DeclarativeBase):
    pass


class Company(CrawlerBase):
    __tablename__ = "company"
    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    company_id: Mapped[str] = mapped_column(String(25), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    link: Mapped[str] = mapped_column(String(300))
    employee: Mapped[str] = mapped_column(String(25), nullable=True)
    jobs: Mapped[List["Job"]] = relationship(
        back_populates="company", cascade="all, delete-orphan"
    )


class Job(CrawlerBase):
    __tablename__ = "job"
    id: Mapped[int] = mapped_column(Integer(), autoincrement=True, primary_key=True)
    job_id: Mapped[str] = mapped_column(String(25), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    link: Mapped[str] = mapped_column(String(300), nullable=False)
    company_id: Mapped[str] = mapped_column(ForeignKey("company.company_id"))
    description: Mapped[str] = mapped_column(String(3000), nullable=True)
    company: Mapped["Company"] = relationship(back_populates="jobs")


class Batch(CrawlerBase):
    __tablename__ = "batch"
    id: Mapped[int] = mapped_column(Integer(), autoincrement=True, primary_key=True)
    batch_id: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    location: Mapped[str] = mapped_column(String(100), nullable=False)
    keywords: Mapped[str] = mapped_column(String(100), nullable=False)
    last_updated: Mapped[datetime.datetime] = mapped_column(
        DateTime(), nullable=False, server_default=func.now()
    )


class BatchRelationship(CrawlerBase):
    __tablename__ = "batch_relationship"
    __table_args__ = (
        UniqueConstraint("batch_id", "job_id", "timestamp", name="unique_index"),
    )
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    batch_id: Mapped[str] = mapped_column(ForeignKey("batch.batch_id"))
    job_id: Mapped[str] = mapped_column(ForeignKey("job.job_id"))
    timestamp: Mapped[datetime.datetime] = mapped_column(
        Date(), server_default=func.current_date()
    )
