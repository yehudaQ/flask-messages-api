from flask import Blueprint
from flask_login import login_required

from app import db
from app.models.user import User

views = Blueprint("views", __name__)


@views.route("/")
def basic():
    return "Messages API basic route"


@views.route("/home", methods=['GET'])
def home():
    return "Home route"


@views.route("/test-login", methods=['GET'])
@login_required
def test():
    return "success"
