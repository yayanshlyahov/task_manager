import os

import settings

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

from todo.index import todo


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://new_user:new_pass@localhost/new_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'testmailbelhard@gmail.com'
app.config['MAIL_PASSWORD'] = 'testmail'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
app.register_blueprint(todo)
db = SQLAlchemy(app)

app.secret_key = '12345678'


from views import * # noqa


if __name__ == '__main__':
    app.run(
        host=settings.HOST,
        port=settings.PORT,
        debug=settings.DEBUG,
    )
