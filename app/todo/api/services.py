from app.todo.model.base import Todo
from .dto.todo_dto import (
    AddTodoRequest,
    MarkTodoDoneRequest,
    TodoResponse,
    UpdateTodoRequest,
    AddTodoResponse,
)
from app.todo.db.todo import insert_todo, query_todos, update_todo, mark_todo_done


def construct_todo_response(item: Todo):
    return TodoResponse(
        id=item.id,
        desc=item.desc,
        created_by=str(item.created_by),
        is_done=item.is_done,
        done_date=str(item.done_date) if item.done_date else None,
        owner=item.owner,
        todos=[construct_todo_response(child) for child in item.children],
    )


def get_todo_service(username: str):
    return [construct_todo_response(item) for item in query_todos(username)]


def add_todo_service(request: AddTodoRequest, username: str):
    new_id = insert_todo(
        Todo(
            desc="",
            parent_task=request.parent_task,
            owner=username,
            is_done=False,
            is_deleted=False,
        )
    )
    return AddTodoResponse(id=new_id)


def update_todo_service(request: UpdateTodoRequest, username: str):
    update_todo(
        id=request.id,
        desc=request.desc,
        is_deleted=request.is_deleted,
        username=username,
    )


def mark_todo_done_service(request: MarkTodoDoneRequest, username: str):
    mark_todo_done(id=request.id, is_done=request.is_done, username=username)
