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

    def __init__(self, subject_id: int, date: datetime, location: str, description: str = None) -> None:
        self.subject_id = subject_id
        self.date = date
        self.location = location
        self.description = description

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_meeting(meeting_id: int) -> Meeting:
        return Meeting.query.filter_by(id=meeting_id).first()
    
    @staticmethod
    def get_all_meetings() -> list[Meeting]:
        return Meeting.query.all()
    
    @staticmethod
    def get_meetings_by_subject(subject_id: int) -> list[Meeting]:
        return Meeting.query.filter_by(subject_id=subject_id).all()
    
    @staticmethod
    def get_meetings_by_date(date: datetime) -> list[Meeting]:
        return Meeting.query.filter_by(date=date).all()
    
    @staticmethod
    def get_meetings_by_location(location: str) -> list[Meeting]:
        return Meeting.query.filter_by(location=location).all()
    
    @staticmethod
    def get_meetings_by_description(description: str) -> list[Meeting]:
        return Meeting.query.filter_by(description=description).all()
    
    @staticmethod
    def get_meetings_by_subject_and_date(subject_id: int, date: datetime) -> list[Meeting]:
        return Meeting.query.filter_by(subject_id=subject_id, date=date).all()
    