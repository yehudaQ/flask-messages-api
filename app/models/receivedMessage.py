from app import db


class ReceivedMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'))
    # message = db.relationship("Message", back_populates="receiver")

    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # receiver = db.relationship("User", back_populates="receivedMessage")

    is_read = db.Column(db.Boolean, default=False)



# class ReceivedMessage(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     message_id = db.Column(db.Integer, db.ForeignKey('message.id'))
#     message = db.relationship("Message", back_populates="receiver")
#
#     receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     receiver = db.relationship("User", back_populates="receivedMessage")
#
#     is_read = db.Column(db.Boolean, default=False)