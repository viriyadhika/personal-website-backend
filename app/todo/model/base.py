from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import (
    Boolean,
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
    done_date: Mapped[datetime.datetime] = mapped_column(Date(), nullable=True)
    children: Mapped[List["Todo"]] = relationship(
        back_populates="parent", cascade="all, delete-orphan", lazy="select"
    )

    parent: Mapped[Optional["Todo"]] = relationship(
        back_populates="children", remote_side=[id]
    )
