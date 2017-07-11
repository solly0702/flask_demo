from server import db
from flask_sqlalchemy import Model
from sqlalchemy import Column, DateTime
from datetime import datetime

class TimestampedModel(Model):
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

FIELD_MAX_LIM = {
    'username': 50,
    'email': 100,
    'password': 150
}

class Users(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(FIELD_MAX_LIM['username']), unique=True, nullable=False)
    email = db.Column(db.String(FIELD_MAX_LIM['email']), unique=True, nullable=False)
    password = db.Column(db.String(FIELD_MAX_LIM['password']), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return "<username %r >" % username
