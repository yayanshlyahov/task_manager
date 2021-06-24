from flask import Blueprint


todo = Blueprint(
    'todo',
    __name__,
    template_folder='templates'
)


@todo.route('/some_route')
def new_route():
    return 'Hello todo bp'
