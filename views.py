from app import app, mail

from flask import request, jsonify, abort, session, render_template
from flask.helpers import make_response
from flask_mail import Message
from model import create_user, get_task, create_task, get_filtered_task, get_users


@app.errorhandler(404)
def error_not_found(error):
    return make_response(
        jsonify({'error': 'task not found'}),
        404
    )


@app.before_request
def is_user_logged_in():
    if 'username' in session:
        print('Authorized')
    else:
        print('Unauthorized')


@app.route('/')
def index():
    # msg = Message('Hello', sender = 'yourId@gmail.com', recipients = ['godyanuss@gmail.com'])
    # msg.body = "This is the email body"
    # mail.send(msg)
   
    return 'Hello world'


@app.route('/api/task/<int:task_id>', methods=['GET'])
def api_get_task(task_id):
    result = get_filtered_task({'id': task_id})
    if len(result) == 0:
        return abort(404)
    return jsonify(result)


@app.route('/api/task/', methods=['POST'])
def add_task():
    import json
    data = json.loads(request.json)
    name = data.get('name')
    descritpion = data.get('description')
    user_id = data.get('user_id')
    if descritpion is not None and name is not None:
        create_task(name, descritpion, user_id)
        return make_response(
            jsonify(
                {
                    'status': 'Ok'
                }
            ), 200)
    if descritpion is None or name is None:
        return make_response(
            jsonify(
                {
                    'status': 'Failed',
                    'Error': 'No description or no name',
                }
            ), 400)


@app.route('/api/task/', methods=['GET'])
def get_tasks():
    return jsonify(get_task())


@app.route('/api/user/<int:user_id>', methods=['GET'])
def api_get_by_user_id(user_id):
    return jsonify(get_filtered_task({'user_id': user_id}))


@app.route('/api/user/', methods=['POST'])
def add_user():
    import json
    data = json.loads(request.json)
    name = data.get('name')
    password = data.get('password')
    yo = data.get('yo')
    if None not in (name, password, yo):
        create_user(name, password, yo)
        return make_response(
            jsonify(
                {
                    'status': 'Ok'
                }
            ), 200)
    return make_response(jsonify(
                {
                    'status': 'Fail'
                }
            ), 400)


@app.route('/api/user/', methods=['GET'])
def get_users_list():
    return jsonify(get_users())


@app.route('/report/user', methods=['GET'])
def generate_report():
    users_list = get_users()
    body = render_template('table.html', result=users_list[0])
    msg = Message('Hello', sender = 'yourId@gmail.com', recipients = ['godyanuss@gmail.com'])
    msg.body = body
    mail.send(msg)
    return 'Message sent'