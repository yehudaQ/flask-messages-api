from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user

from app import db
from app.models.message import Message
from app.models.receivedMessage import ReceivedMessage
from app.models.user import User

message = Blueprint("message", __name__)


@message.route("/message", methods=['GET', 'POST'])
@login_required
def messages():
    if request.method == 'POST':
        receiver_email = request.form.get("receiver_email")
        message = request.form.get("message")
        subject = request.form.get("subject")

        receiver = User.query.filter_by(email=receiver_email).first()

        if not receiver:
            return 'Receiver Email is not exists.', 403

        new_message = Message(message=message, subject=subject, sender_id=current_user.id)
        db.session.add(new_message)
        db.session.commit()

        received_message = ReceivedMessage(message_id=new_message.id, receiver_id=receiver.id)
        db.session.add(received_message)
        db.session.commit()

        return 'Message successfully created.', 201

    # GET method - Retrieve all user's received messages
    user = User.query.filter_by(id=current_user.id).first()
    received_messages = user.received_messages

    return jsonify([received.message.serialize for received in received_messages]), 200


@message.route("/message/sent", methods=['GET'])
@login_required
def get_sent_messages():
    user = User.query.filter_by(id=current_user.id).first()
    sent_messages = user.sent_messages

    return jsonify([msg.serialize for msg in sent_messages]), 200


@message.route("/message/unread", methods=['GET'])
@login_required
def get_unread_messages():
    received_messages = ReceivedMessage.query.filter_by(receiver_id=current_user.id, is_read=False).all()

    return jsonify([received.message.serialize for received in received_messages]), 200


@message.route("/message/read/<int:message_id>", methods=['PATCH'])
@login_required
def read_message(message_id):
    receive_message = ReceivedMessage.query.filter_by(receiver_id=current_user.id, message_id=message_id).first()

    if not message:
        return "Message not found.", 404

    message.is_read = True
    db.session.commit()

    return jsonify(receive_message.message.serialize), 200
