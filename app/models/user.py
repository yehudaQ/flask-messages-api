from flask_login import UserMixin
from app import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

    sent_messages = db.relationship("Message", backref='sender', cascade="all")
    received_messages = db.relationship("ReceivedMessage", backref='receiver', cascade="all")

    def __repr__(self):
        return f'User : {self.id} : {self.email}'
