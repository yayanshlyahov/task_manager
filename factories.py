# from app import db
import random
from model import create_task


def create_task_with_data(**kwargs):
    name = str(
        random.randint(100, 1000)
    )
    description = str(random.randint(1000, 10000))
    data = {
        'new_name': name,
        'new_description': description,
        'user_id': None,
        **kwargs
    }
    create_task(**data)
