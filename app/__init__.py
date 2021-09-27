from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

from app.core.utils import get_configs_as_dictionary

db = SQLAlchemy()
config = get_configs_as_dictionary()
DB_NAME = config['DB_NAME']
DB_URI = config['SQLALCHEMY_DATABASE_URI']


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = config['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = f'{DB_URI}{DB_NAME}'
    db.init_app(app)

    from app.api.views import views
    from app.api.auth.auth import auth
    from app.api.message.views import message

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(message, url_prefix="/")

    from app.models.user import User
    from app.models.message import Message
    from app.models.receivedMessage import ReceivedMessage

    create_database(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists(f'app/{DB_NAME}'):
        db.create_all(app=app)
        print("Created database!")
