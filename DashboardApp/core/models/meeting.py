from __future__ import annotations
from datetime import datetime
from DashboardApp import db


class Meeting(db.Model):
    __tablename__ = "meeting"

    # identifiers
    id = db.Column(db.Integer, primary_key=True)
    created_timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now())

    # meeting details
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(256), nullable=True, default=None)

    # meeting content
    deliverables = db.relationship("Deliverable", backref="meeting", lazy=True)
