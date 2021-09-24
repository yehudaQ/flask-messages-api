from flask import Blueprint
from werkzeug.security import generate_password_hash

from app import db
from app.models.user import User

views = Blueprint("views", __name__)


@views.route("/")
def basic():
    return "Messages API basic route"


@views.route("/home", methods=['GET'])
def home():
    return "Home route"


@views.route("/test", methods=['POST'])
def test():
    new_user = User(email="yehuda1234@gmail.com", password=generate_password_hash(
        "mypass", method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return {}
