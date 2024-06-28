from __future__ import annotations
from datetime import datetime
from DashboardApp import db
from sqlalchemy.orm import Query
from typing import Dict, List


class Meeting(db.Model):
    __tablename__ = "meeting"

    # identifiers
    id = db.Column(db.Integer, primary_key=True)
    created_timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now())
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    # meeting details
    name = db.Column(db.String(16), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(256), nullable=True, default=None)

    # meeting content
    deliverables = db.relationship("Deliverable", backref="meeting", lazy=True)

    def __init__(
        self,
        owner_id: int,
        name: str,
        subject_id: int,
        date: datetime,
        location: str,
        description: str = None,
    ) -> None:
        self.owner_id = owner_id
        self.name = name
        self.subject_id = subject_id
        self.date = date
        self.location = location
        self.description = description

    def __repr__(self) -> str:
        return self.name

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "created_timestamp": self.created_timestamp,
            "owner_id": self.owner_id,
            "name": self.name,
            "subject_id": self.subject_id,
            "date": self.date,
            "location": self.location,
            "description": self.description,
        }

    def limit_query_to_owner(owner_id: int) -> Query:
        return Meeting.query.filter_by(owner_id=owner_id)

    @staticmethod
    def get_meeting(owner_id: int, id: int) -> Meeting:
        return Meeting.limit_query_to_owner(owner_id).filter_by(id=id).first()

    @staticmethod
    def get_all_meetings(owner_id: int) -> List[Meeting]:
        return Meeting.limit_query_to_owner(owner_id).all()

    @staticmethod
    def meeting_exists(owner_id: int, name: str) -> bool:
        return Meeting.limit_query_to_owner(owner_id).filter_by(name=name).first() is not None

    @staticmethod
    def get_meeting_by_id(owner_id: int, id: int) -> Meeting:
        return Meeting.limit_query_to_owner(owner_id).filter_by(id=id).first()

    @staticmethod
    def get_meeting_by_name(owner_id: int, name: str) -> Meeting:
        return Meeting.limit_query_to_owner(owner_id).filter_by(name=name).first()

    @staticmethod
    def get_meetings_by_subject(owner_id: int, subject_id: int) -> List[Meeting]:
        return Meeting.limit_query_to_owner(owner_id).filter_by(subject_id=subject_id).all()

    @staticmethod
    def get_meetings_by_date(owner_id: int, date: datetime) -> List[Meeting]:
        return Meeting.limit_query_to_owner(owner_id).filter_by(date=date).all()

    @staticmethod
    def get_meetings_by_location(owner_id: int, location: str) -> List[Meeting]:
        return Meeting.limit_query_to_owner(owner_id).filter_by(location=location).all()

    @staticmethod
    def get_meetings_by_description(owner_id: int, description: str) -> List[Meeting]:
        return Meeting.limit_query_to_owner(owner_id).filter_by(description=description).all()

    @staticmethod
    def get_meetings_by_subject_and_date(owner_id: int, subject_id: int, date: datetime) -> List[Meeting]:
        return Meeting.limit_query_to_owner(owner_id).filter_by(subject_id=subject_id, date=date).all()
