import flask
from .router import main

def init_router(app: flask.Flask):
    app.register_blueprint(main)
