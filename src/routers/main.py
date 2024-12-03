import flask
from .router import main
from .todo_list import todo_list


def init_router(app: flask.Flask):
    app.register_blueprint(main)
    app.register_blueprint(todo_list)
