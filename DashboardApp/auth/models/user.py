# DashboardApp/auth/models/user.py
from flask import current_app
from datetime import datetime

db = current_app.extensions['sqlalchemy'].db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now())
    user_name = db.Column(db.String(16), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)
