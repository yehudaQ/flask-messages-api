from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path, remove

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
    app.register_blueprint(views, url_prefix="/")

    from app.models.user import User
    from app.models.receivedMessage import ReceivedMessage
    from app.models.message import Message
    create_database(app)

    return app


def create_database(app):
    if not path.exists(f'app/{DB_NAME}'):
        db.create_all(app=app)
        print("Created database!")

    # TODO : Remove 'else' statment
    else:
        remove("app/" + DB_NAME)
        print("Database dropped!")
        db.create_all(app=app)
        print("Created database!")
