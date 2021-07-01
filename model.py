from app import db


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


if __name__ == "__main__":
    # db.metadata.clear()
    print("Creating database tables...")
    db.create_all()
    print("Done!")
