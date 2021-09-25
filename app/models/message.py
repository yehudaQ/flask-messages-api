from app import db
from datetime import datetime


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255), unique=True)
    subject = db.Column(db.String(150), unique=True)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)

    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # sender = db.relationship("User", back_populates="sentMessages")

    # received_messages = db.relationship("ReceivedMessage", back_populates='message', cascade="all")

#
# class Message(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     message = db.Column(db.String(255), unique=True)
#     subject = db.Column(db.String(150), unique=True)
#     creation_date = db.Column(db.DateTime, default=datetime.utcnow)
#
#     sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     sender = db.relationship("User", back_populates="sentMessages")
#
#     receivedMsg = db.relationship("ReceivedMessage", back_populates='message', cascade="all")