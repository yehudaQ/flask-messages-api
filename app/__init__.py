from flask import Flask

from app.api.views import views
from app.core.utils import get_configs_as_dictionary


def create_app():
    app = Flask(__name__)
    config = get_configs_as_dictionary()
    app.config['SECRET_KEY'] = config['SECRET_KEY']

    app.register_blueprint(views, url_prefix="/")

    return app
