from app import db
from datetime import datetime


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255))
    subject = db.Column(db.String(150))
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)

    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    received_messages = db.relationship("ReceivedMessage", backref='message', cascade="all")

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'message': self.message,
            'subject': self.subject,
            'creation_date': str(self.creation_date),
            'sender_id': self.sender_id
        }
