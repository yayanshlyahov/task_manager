import os

import settings

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from todo.index import todo


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
