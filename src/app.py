from flask import Flask
from dotenv import load_dotenv, find_dotenv
from .config import app_config
from .models import db

load_dotenv(find_dotenv())


def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])

    from .routes import api
    from .models import HierarchyModel

    db.init_app(app)
    api.init_app(app)

    return app
