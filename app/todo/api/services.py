from typing import List
from datetime import datetime, timezone
from app.auth.services.user import get_user_based_on_username
from app.todo.model.base import Todo
from .dto.todo_dto import (
    AddTodoRequest,
    GetReminderResponse,
    MarkTodoDoneRequest,
    TodoResponse,
    UpdateTodoRequest,
    AddTodoResponse,
    AddReminderRequest,
    UpdateTodoPriorityRequest
)
from app.common.bot.bot import bot
from app.todo.db.todo import (
    get_reminder_time,
    insert_todo,
    query_todos,
    remove_reminder,
    update_todo,
    mark_todo_done,
    add_reminder,
    read_reminder,
    get_journal,
    delete_todo,
    update_priority,
    TodoPriorityUpdate
)
import logging

logger = logging.getLogger(__name__)


def construct_todo_response(item: Todo, username: str):
    return TodoResponse(
        id=item.id,
        desc=item.desc,
        created_by=str(item.created_by),
        is_done=item.is_done,
        done_date=str(item.done_date) if item.done_date else None,
        owner=item.owner,
        todos=[construct_todo_response(child, username) for child in query_todos(username, item.id)],
        priority=item.priority
    )


def get_todo_service(username: str):
    return [construct_todo_response(item, username) for item in query_todos(username, None)]


def add_todo_service(request: AddTodoRequest, username: str):
    todos = query_todos(username, request.parent_task)
    max_priority = max([item.priority for item in todos]) if len(todos) > 0 else -1
    new_id = insert_todo(
        Todo(
            desc="",
            parent_task=request.parent_task,
            owner=username,
            is_done=False,
            is_deleted=False,
            priority=max_priority + 1
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

def update_priority_service(requests: List[UpdateTodoPriorityRequest], username: str):
    update_priority(
        todo_priority_updates=[TodoPriorityUpdate(
            id=request.id,
            priority=request.priority
        ) for request in requests],
        username=username,
    )

def delete_todo_service(id: int, username: str):
    delete_todo(id=id, username=username)


def mark_todo_done_service(request: MarkTodoDoneRequest, username: str):
    mark_todo_done(id=request.id, is_done=request.is_done, username=username)


def add_reminder_service(request: AddReminderRequest, username: str):
    if request.time == None:
        add_reminder(request.todo_id, None, username)
        return
    time = datetime.fromtimestamp(request.time, tz=timezone.utc).replace(tzinfo=None)
    add_reminder(request.todo_id, time, username)


async def run_reminder_service():
    all_reminders = read_reminder()
    logger.info(f"read {len(all_reminders)} reminders")
    mapping = {}
    for reminder in all_reminders:
        reminder_id, todo = reminder
        user = (
            get_user_based_on_username(todo.owner)
            if todo.owner not in mapping
            else mapping[todo.owner]
        )
        mapping[todo.owner] = user

        if not user.tele_id:
            continue

        await bot.app.bot.send_message(user.tele_id, f"TODO: {todo.desc}")
        remove_reminder(reminder_id)


def get_reminder_service(todo_id: int, username: str):
    time = get_reminder_time(todo_id, username)
    if time == None:
        return GetReminderResponse(time=None)
    return GetReminderResponse(time=int(time.replace(tzinfo=timezone.utc).timestamp()))


def get_journal_service(username: str):
    return [
        TodoResponse(
            id=item.id,
            desc=item.desc,
            created_by=str(item.created_by),
            is_done=item.is_done,
            done_date=str(item.done_date) if item.done_date else None,
            owner=item.owner,
            todos=[],
            priority=item.priority
        )
        for item in get_journal(username)
    ]
