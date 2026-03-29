from datetime import datetime
from backend.extensions import db


class ContactMessage(db.Model):
    __tablename__ = "contact_messages"

    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(120), nullable=False)
    email      = db.Column(db.String(254), nullable=False)
    message    = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
