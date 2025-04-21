from app.db.engine import engine
from sqlalchemy.orm import Session
from sqlalchemy import insert, select, update
from app.todo.model.base import Todo
from sqlalchemy.orm import selectinload, with_loader_criteria
from datetime import datetime


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
