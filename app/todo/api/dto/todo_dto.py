from __future__ import annotations
from typing import List, Optional
from unittest.mock import Base
from pydantic import BaseModel


class TodoResponse(BaseModel):
    id: int
    desc: str
    created_by: str
    owner: str
    is_done: bool
    done_date: Optional[str]
    priority: int
    todos: List["TodoResponse"]

    model_config = {"from_attributes": True}


class AddTodoRequest(BaseModel):
    parent_task: Optional[int]


class AddTodoResponse(BaseModel):
    id: int


class UpdateTodoRequest(BaseModel):
    desc: str
    is_deleted: bool
    id: int

class UpdateTodoPriorityRequest(BaseModel):
    priority: int
    id: int

class DeleteTodoRequest(BaseModel):
    id: int


class MarkTodoDoneRequest(BaseModel):
    is_done: bool
    id: int


class AddReminderRequest(BaseModel):
    time: Optional[int]
    todo_id: int


class GetReminderRequest(BaseModel):
    todo_id: int


class GetReminderResponse(BaseModel):
    time: Optional[int]
