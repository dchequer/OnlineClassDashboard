from __future__ import annotations
from datetime import datetime
from DashboardApp import db

class Deliverable(db.Model):
    __tablename__ = 'deliverable'

    # identifiers
    id = db.Column(db.Integer, primary_key=True)
    created_timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now())

    # deliverable details
    title = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    assigned_date = db.Column(db.DateTime, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    meeting_id = db.Column(db.Integer, db.ForeignKey('meeting'), nullable=False)
    status = db.Column(db.String(16), nullable=False, default='pending')
    grade = db.Column(db.Integer, nullable=True, default=None)

    # deliverable content


    def __init__(self, title: str, description: str, assigned_date: datetime, due_date: datetime, subject_id: int, meeting_id: int) -> None:
        self.title = title
        self.description = description
        self.assigned_date = assigned_date
        self.due_date = due_date
        self.subject_id = subject_id
        self.meeting_id = meeting_id