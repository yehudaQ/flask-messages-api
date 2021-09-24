from app import db


class ReceivedMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'))
    message = db.relationship("Message", backref="receivedmessage")

    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiver = db.relationship("User", backref="receivedmessage")

    is_read = db.Column(db.Boolean, default=False)
