from flask import Blueprint

views = Blueprint("views", __name__)


@views.route("/")
def basic():
    return "Messages API basic route"


@views.route("/home", methods=['GET'])
def home():
    return "Home route"
