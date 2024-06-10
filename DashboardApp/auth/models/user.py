# DashboardApp/auth/models/user.py
from datetime import datetime
from DashboardApp import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    created_timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now())
    user_name = db.Column(db.String(16), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
    
    def save(self):
        db.session.add(self)
        db.session.commit()