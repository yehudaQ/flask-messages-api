from flask import Blueprint
from flask_login import login_required

views = Blueprint("views", __name__)


@views.route("/", methods=['GET'])
def basic():
    return "Messages API basic route"


@views.route("/home", methods=['GET'])
def home():
    return "Home route"


@views.route("/test-login", methods=['GET'])
@login_required
def test():
    return "success"
