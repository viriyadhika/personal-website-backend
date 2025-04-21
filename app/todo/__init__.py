from typing import Annotated

from app.common.dto.user import UserDto
from fastapi import APIRouter, Depends
from app.common.auth.jwt import get_current_user

from app.todo.api.dto.todo_dto import (
    AddTodoRequest,
    MarkTodoDoneRequest,
    UpdateTodoRequest,
)
from app.todo.api.services import (
    add_todo_service,
    get_todo_service,
    update_todo_service,
    mark_todo_done_service,
)

todo_router = APIRouter(prefix="/api/todo")


@todo_router.post("/add")
def add_todo(
    request: AddTodoRequest, current_user: Annotated[UserDto, Depends(get_current_user)]
):
    return add_todo_service(request, current_user.username)


@todo_router.get("/list")
def get_todos(current_user: Annotated[UserDto, Depends(get_current_user)]):
    return get_todo_service(current_user.username)


@todo_router.post("/update")
def update_todos(
    request: UpdateTodoRequest,
    current_user: Annotated[UserDto, Depends(get_current_user)],
):
    update_todo_service(request, current_user.username)
    return {"status": "success"}


@todo_router.post("/done")
def mark_done_todos(
    request: MarkTodoDoneRequest,
    current_user: Annotated[UserDto, Depends(get_current_user)],
):
    mark_todo_done_service(request, current_user.username)
    return {"status": "success"}
