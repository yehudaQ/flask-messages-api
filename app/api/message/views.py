from flask import Blueprint, request
from flask_login import login_required, current_user

from app import db
from app.models.message import Message
from app.models.user import User

message = Blueprint("message", __name__)


@message.route("/message", methods=['GET'])
@login_required
def basic():
    return "Messages Views API basic route"


@message.route("/message", methods=['GET', 'POST'])
@login_required
def create_message():
    if request.method == 'POST':
        print(request.form)
        receiver_email = request.form.get("receiver_email")
        message = request.form.get("message")
        subject = request.form.get("subject")

        receiver = User.query.filter_by(email=receiver_email).first()

        if not receiver:
            return 'Receiver Email is not exists.', 403

        print(current_user)
        new_message = Message(message=message, subject=subject, sender_id=current_user.id)
        db.session.add(new_message)
        db.session.commit()

        return 'Message successfully created.', 201
