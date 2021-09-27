from flask import Blueprint
from werkzeug.security import generate_password_hash

from app import db
from app.models.message import Message
from app.models.receivedMessage import ReceivedMessage
from app.models.user import User

views = Blueprint("views", __name__)


@views.route("/", methods=['GET'])
def basic():
    return "Messages API basic route"


@views.route("/home", methods=['GET'])
def home():
    return "Home route"


@views.route("/mock", methods=['GET'])
def test():
    # TODO - Delete function
    from app.models.user import User
    new_user1 = User(email="yehuda1@gmail.com", password=generate_password_hash("1234567", method='sha256'))
    new_user2 = User(email="linoy@gmail.com", password=generate_password_hash("12345678", method='sha256'))
    new_user3 = User(email="yuval@gmail.com", password=generate_password_hash("123456789", method='sha256'))

    db.session.add(new_user1)
    db.session.add(new_user2)
    db.session.add(new_user3)
    db.session.commit()

    create_message_mock(new_user2.email, f'message 1 from {new_user1.email} to {new_user2.email}', "test message 1",
                        new_user1.id)
    create_message_mock(new_user3.email, f'message 2 from {new_user1.email} to {new_user3.email}', "test message 2",
                        new_user1.id)

    create_message_mock(new_user3.email, f'message 3 from {new_user2.email} to {new_user3.email}', "test message 3",
                        new_user2.id)
    create_message_mock(new_user1.email, f'message 4 from {new_user2.email} to {new_user1.email}', "test message 4",
                        new_user2.id)

    create_message_mock(new_user1.email, f'message 5 from {new_user3.email} to {new_user1.email}', "test message 5",
                        new_user3.id)
    create_message_mock(new_user2.email, f'message 6 from {new_user3.email} to {new_user2.email}', "test message 6",
                        new_user3.id)
    return "success"


def create_message_mock(receiver_email, message, subject, sender_id):
    receiver = User.query.filter_by(email=receiver_email).first()

    if not receiver:
        return 'Receiver Email is not exists.', 403

    new_message = Message(message=message, subject=subject, sender_id=sender_id)
    db.session.add(new_message)
    db.session.commit()

    received_message = ReceivedMessage(message_id=new_message.id, receiver_id=receiver.id)
    db.session.add(received_message)
    db.session.commit()
