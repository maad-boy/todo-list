from config import init_config, get_config
from src import init_router, init_db
from flask import Flask

def run_app():
    app = Flask(__name__)

    init_config("config/config.yaml")
    _config = get_config()

    init_db(app=app)
    init_router(app)

    app.run(_config.service.host, _config.service.port, _config.service.debug)

