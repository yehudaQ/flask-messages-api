from flask import Blueprint

views = Blueprint("views", __name__)


@views.route("/home", methods=['GET'])
def basic():
    return "Messages API basic route"
