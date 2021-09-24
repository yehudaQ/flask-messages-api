from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

    receivedMsg = db.relationship("ReceivedMessage", backref='user', cascade="all")
    sentMsg = db.relationship("Message", backref='user', cascade="all")
