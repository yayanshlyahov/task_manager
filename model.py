from app import db


class Task(db.Model):
    __table_args__ = {'extend_existing': True} 
    
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
    __table_args__ = {'extend_existing': True} 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(250))
    yo = db.Column(db.Integer)
    phone_number = db.Column(db.Integer)

    def __init__(self, name, password, yo):
        self.name = name
        self.password = hash(password)
        self.yo = yo


def create_user(new_name, new_password, new_yo):
    user = User(new_name, new_password, new_yo)
    db.session.add(user)
    db.session.commit()
    return user


def get_users():
    user_list = []
    for user in User.query.all():
        current_user = {
            'id': user.id,
            'name': user.name,
            'password': user.password,
            'yo': user.yo,
        }
        user_list.append(current_user)
    return user_list 


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
    # db.metadata.clear()
    print("Creating database tables...")
    db.create_all()
    print("Done!")
