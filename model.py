from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(250))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", backref=db.backref("user", uselist=False))

    def __init__(self, name, description, user_id=None):
        self.name = name
        self.description = description
        self.user_id = user_id


def create_task(new_name, new_description, user_id):
    task = Task(new_name, new_description, user_id)
    db.session.add(task)
    db.session.commit()
    return task


def get_task(id=None):
    if id:
        tasks = Task.query.filter_by(id=id).all()
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


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(250))

    def __init__(self, name, password):
        self.name = name
        self.password = hash(password)


def create_user(new_name, new_password):
    user = User(new_name, new_password)
    db.session.add(user)
    db.session.commit()
    return user


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


if __name__ == "__main__":
    print("Creating database tables...")
    db.create_all()
    print("Done!")
