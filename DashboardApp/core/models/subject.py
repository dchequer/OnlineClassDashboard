from __future__ import annotations
from datetime import datetime
from DashboardApp import db

class Subject(db.Model):
    __tablename__ = 'subject'

    # identifiers
    id = db.Column(db.Integer, primary_key=True)
    created_timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now())

    # subject details
    name = db.Column(db.String(16), nullable=False, unique=True)
    code = db.Column(db.String(8), nullable=False, unique=True)
    instructor = db.Column(db.String(16), nullable=False)
    contact_info = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(32), nullable=True, default=None)

    # subject content
    announcements = db.relationship('Announcement', backref='subject', lazy=True)
    deliverables = db.relationship('Deliverable', backref='subject', lazy=True)
    meetings = db.relationship('Meeting', backref='subject', lazy=True)


