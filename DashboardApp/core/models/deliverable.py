from __future__ import annotations
from datetime import datetime
from typing import List
from DashboardApp import db
from .subject import Subject
from sqlalchemy.orm import Query


class Deliverable(db.Model):
    __tablename__ = "deliverable"

    # identifiers
    id = db.Column(db.Integer, primary_key=True)
    created_timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now())
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    # deliverable details
    title = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    assigned_date = db.Column(db.DateTime, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"), nullable=True)
    meeting_id = db.Column(db.Integer, db.ForeignKey("meeting.id"), nullable=True)
    status = db.Column(db.String(16), nullable=False, default="pending")
    grade = db.Column(db.Integer, nullable=True, default=None)

    # deliverable content

    def __init__(
        self,
        owner_id: int,
        title: str,
        description: str,
        assigned_date: datetime,
        due_date: datetime,
        subject_id: int,
        meeting_id: int,
    ) -> None:
        self.owner_id = owner_id
        self.title = title
        self.description = description
        self.assigned_date = assigned_date
        self.due_date = due_date
        self.subject_id = subject_id
        self.meeting_id = meeting_id

    def __repr__(self) -> str:
        return self.title

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def limit_query_to_owner(owner_id: int) -> Query:
        return Deliverable.query.filter_by(owner_id=owner_id)

    @staticmethod
    def deliverable_exists(owner_id: int, title: str) -> bool:
        return (
            Deliverable.limit_query_to_owner(owner_id).filter_by(title=title).first()
            is not None
        )

    @staticmethod
    def get_deliverable(owner_id: int, deliverable_id: int) -> Deliverable:
        return (
            Deliverable.limit_query_to_owner(owner_id)
            .filter_by(id=deliverable_id)
            .first()
        )

    @staticmethod
    def get_deliverable_by_title(owner_id: int, title: str) -> Deliverable:
        return Deliverable.limit_query_to_owner(owner_id).filter_by(title=title).first()

    @staticmethod
    def get_all_deliverables(owner_id: int) -> list[Deliverable]:
        return Deliverable.limit_query_to_owner(owner_id).all()

    @staticmethod
    def get_deliverables_by_subject(
        owner_id: int, subject_id: int
    ) -> list[Deliverable]:
        return (
            Deliverable.limit_query_to_owner(owner_id)
            .filter_by(subject_id=subject_id)
            .all()
        )

    @staticmethod
    def get_deliverables_by_meeting(
        owner_id: int, meeting_id: int
    ) -> list[Deliverable]:
        return (
            Deliverable.limit_query_to_owner(owner_id)
            .filter_by(meeting_id=meeting_id)
            .all()
        )

    @staticmethod
    def search_deliverables(owner_id: int, search_term: str) -> list[Deliverable]:
        return (
            Deliverable.limit_query_to_owner(owner_id)
            .filter_by(Deliverable.title.ilike(f"%{search_term}%"))
            .all()
        )

    @staticmethod
    def get_deliverables_by_status(owner_id: int, status: str) -> list[Deliverable]:
        return (
            Deliverable.limit_query_to_owner(owner_id=owner_id)
            .filter_by(status=status)
            .all()
        )
