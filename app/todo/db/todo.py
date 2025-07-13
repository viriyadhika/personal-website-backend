from typing import Optional
from app.db.engine import engine
from sqlalchemy.orm import Session
from sqlalchemy import delete, select, update, desc
from app.todo.model.base import Reminder, Todo
from sqlalchemy.orm import selectinload, with_loader_criteria
from datetime import datetime, timezone


def query_todos(username: str):
    with Session(engine) as session:
        try:
            statement = (
                select(Todo)
                .options(
                    selectinload(Todo.children).selectinload(Todo.children),
                    with_loader_criteria(Todo, Todo.is_deleted == False),
                )
                .where(
                    Todo.owner == username,
                    Todo.is_deleted == False,
                    Todo.parent_task == None,
                )
            )
            ptimes = session.scalars(statement).fetchall()

            return ptimes
        except Exception as err:
            print(f"Error querying todos {err}")


def insert_todo(todo: Todo):
    with Session(engine) as session:
        try:
            print(f"Insert todo {todo.__dict__}")
            session.add(todo)
            session.commit()
            return todo.id
        except Exception as err:
            print(f"Error inserting todos {err}")
            raise


def check_user(session: Session, todo_id: int, username: str):
    statement = select(Todo).where(Todo.id == todo_id)
    todo_item = session.scalar(statement)
    if todo_item is None:
        raise Exception("Todo item doesn't exist")
    if todo_item.owner != username:
        raise Exception("User is not authorized to perform action")


def update_todo(id: int, desc: str, is_deleted: bool, username: str):
    with Session(engine) as session:
        check_user(session, id, username)
        try:
            statement = (
                update(Todo)
                .where(Todo.id == id)
                .values(desc=desc, is_deleted=is_deleted)
            )
            session.execute(statement)
            session.commit()
        except Exception as err:
            print(f"Error updating todos {err}")
            raise


def delete_todo(id: int, username: str):
    with Session(engine) as session:
        check_user(session, id, username)
        try:
            statement = delete(Todo).where(Todo.id == id)
            session.execute(statement)
            session.commit()
        except Exception as err:
            print(f"Error updating todos {err}")
            raise


def mark_todo_done(id: int, is_done: bool, username: str):
    with Session(engine) as session:
        check_user(session, id, username)
        try:
            if is_done:
                statement = (
                    update(Todo)
                    .where(Todo.id == id)
                    .values(is_done=True, done_date=datetime.now())
                )
                session.execute(statement)
            else:
                statement = (
                    update(Todo)
                    .where(Todo.id == id)
                    .values(is_done=False, done_date=None)
                )
                session.execute(statement)

            session.commit()
        except Exception as err:
            print(f"Error updating todos {err}")
            raise


def add_reminder(todo_id: int, time: Optional[datetime], username: str):
    with Session(engine) as session:
        try:
            check_user(session, todo_id, username)
            statement = select(Reminder).where(Reminder.todo_id == todo_id)
            existing_reminder = session.scalar(statement)
            if time == None:
                del_stmt = delete(Reminder).where(Todo.id == todo_id)
                session.execute(del_stmt)
            elif existing_reminder != None:
                update_stmnt = (
                    update(Reminder)
                    .where(Reminder.id == existing_reminder.id)
                    .values(time=time)
                )
                session.execute(update_stmnt)
            else:
                new_reminder = Reminder(todo_id=todo_id, time=time)
                session.add(new_reminder)

            session.commit()
        except Exception as err:
            print(f"Error adding reminder {err}")
            raise


def read_reminder():
    with Session(engine) as session:
        try:
            statement = (
                select(Reminder.id, Todo)
                .join_from(Reminder, Todo)
                .where(
                    Reminder.time < datetime.now(tz=timezone.utc).replace(tzinfo=None)
                )
            )
            result = session.execute(statement).fetchall()
            return [item.tuple() for item in result]
        except Exception as err:
            print(f"Error reading reminder {err}")
            raise


def remove_reminder(reminder_id: int):
    with Session(engine) as session:
        try:
            statement = delete(Reminder).where(Reminder.id == reminder_id)
            session.execute(statement)
            session.commit()
        except Exception as err:
            print(f"Error removing reminder {err}")
            raise


def get_reminder_time(todo_id: int, username: str):
    with Session(engine) as session:
        try:
            check_user(session, todo_id, username)
            statement = select(Reminder.time).where(Reminder.todo_id == todo_id)
            return session.scalar(statement)
        except Exception as err:
            print(f"Error getting reminder {err}")
            raise


def get_journal(username: str):
    with Session(engine) as session:
        try:
            statement = (
                select(Todo)
                .where(Todo.owner == username, Todo.is_done == True)
                .order_by(desc(Todo.done_date))
            )
            return session.scalars(statement).fetchall()
        except Exception as err:
            print(f"Error getting journal {err}")
            raise
