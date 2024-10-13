import config
from src import routers
from flask import Flask

def run_app():
    config.init_config("config/config.yaml")
    _config = config.get_config()
    app = Flask(__name__)
    routers.init_router(app)
    app.run(_config.service.host, _config.service.port, _config.service.debug)

