from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import (
    Boolean,
    DateTime,
    Integer,
    String,
    ForeignKey,
    Date,
)
from sqlalchemy.orm import mapped_column, Mapped, relationship
import datetime
from typing import List, Optional
from sqlalchemy.sql import func


class TodoBase(DeclarativeBase):
    pass


class Todo(TodoBase):
    __tablename__ = "todo"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    desc: Mapped[str] = mapped_column(String(500), nullable=False)
    created_by: Mapped[datetime.datetime] = mapped_column(
        Date(), server_default=func.current_date()
    )
    parent_task: Mapped[int] = mapped_column(ForeignKey("todo.id"), nullable=True)
    owner: Mapped[str] = mapped_column(String(100), nullable=False)
    is_done: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    is_deleted: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    priority: Mapped[int] = mapped_column(Integer, nullable=False)
    done_date: Mapped[datetime.datetime] = mapped_column(Date(), nullable=True)


class Reminder(TodoBase):
    __tablename__ = "todo_reminder"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    todo_id: Mapped[int] = mapped_column(ForeignKey("todo.id"))
    time: Mapped[datetime.datetime] = mapped_column(DateTime())
