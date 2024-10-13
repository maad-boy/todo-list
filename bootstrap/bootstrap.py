import config
from src import routers, database
from flask import Flask

def run_app():
    app = Flask(__name__)

    config.init_config("config/config.yaml")
    _config = config.get_config()

    database.init_db(app=app)
    routers.init_router(app)

    app.run(_config.service.host, _config.service.port, _config.service.debug)

