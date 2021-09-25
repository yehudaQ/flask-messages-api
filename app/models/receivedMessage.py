from app import db


class ReceivedMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    is_read = db.Column(db.Boolean, default=False)

