from app import app

from flask import request, jsonify, abort, session
from flask.helpers import make_response
from model import get_task, create_task, get_filtered_task


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
        abort(403)


@app.route('/')
def index():
    session['username'] = 'Vasya'
    return 'Hello world'


@app.route('/api/task/<int:task_id>', methods=['GET'])
def api_get_task(task_id):
    result = get_filtered_task({'id': task_id})
    if len(result) == 0:
        return abort(404)
    return jsonify(result)


@app.route('/api/task/', methods=['POST'])
def add_task():
    data = request.json
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
