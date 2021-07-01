from app import db
from model import User, Task
from pydantic_sqlalchemy import sqlalchemy_to_pydantic


PydanticUser = sqlalchemy_to_pydantic(User)
PydanticTask = sqlalchemy_to_pydantic(Task)


def create_task(new_name, new_description, user_id):
    task = Task(new_name, new_description, user_id)
    db.session.add(task)
    db.session.commit()
    return task


def get_task(id=None):
    if id:
        tasks = Task.query.filter_by(id=id).first()
        pydantic_task = PydanticUser.from_orm(tasks)
        return pydantic_task.dict()
    else:
        tasks = Task.query.all()
    tasks_list = []
    for task in tasks:
        current_task = {
            'id': task.id,
            'name': task.name,
            'description': task.description,
            'user_id': task.user.name if task.user else None
        }
        tasks_list.append(current_task)
    return tasks_list


def create_user(new_name, new_password, new_yo):
    user = User(new_name, new_password, new_yo)
    db.session.add(user)
    db.session.commit()
    return user


def get_users():
    user = User.query.first()
    pydantic_user = PydanticUser.from_orm(user)
    return pydantic_user.dict()


def get_filtered_task(kwargs):
    if kwargs:
        tasks = Task.query.filter_by(**kwargs).all()
    else:
        return []
    tasks_list = []
    for task in tasks:
        current_task = {
            'id': task.id,
            'name': task.name,
            'description': task.description,
            'user_id': task.user.name if task.user else None
        }
        tasks_list.append(current_task)
    return tasks_list
