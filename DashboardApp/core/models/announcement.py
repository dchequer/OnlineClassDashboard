from __future__ import annotations
from datetime import datetime
from DashboardApp import db

class Announcement(db.Model):
    __tablename__ = 'announcement'

    # identifiers
    id = db.Column(db.Integer, primary_key=True)
    created_timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now())

    # announcement details
    title = db.Column(db.String(32), nullable=False)
    content = db.Column(db.String(256), nullable=False)
    author = db.Column(db.String(16), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)

    