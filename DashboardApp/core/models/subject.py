from __future__ import annotations
from datetime import datetime
from DashboardApp import db
from typing import List, Dict
from sqlalchemy.orm import Query


class Subject(db.Model):
    __tablename__ = "subject"

    # identifiers
    id = db.Column(db.Integer, primary_key=True)
    created_timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now())
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    # subject details
    name = db.Column(db.String(16), nullable=False)
    code = db.Column(db.String(8), nullable=False)
    instructor = db.Column(db.String(16), nullable=False)
    contact_info = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(32), nullable=True, default=None)

    # subject content
    announcements = db.relationship("Announcement", backref="subject", lazy=True)
    deliverables = db.relationship("Deliverable", backref="subject", lazy=True)
    meetings = db.relationship("Meeting", backref="subject", lazy=True)

    def __init__(
        self,
        owner_id: int,
        name: str,
        code: str,
        instructor: str,
        contact_info: str,
        description: str = None,
    ):
        self.owner_id = owner_id
        self.name = name
        self.code = code
        self.instructor = instructor
        self.contact_info = contact_info
        self.description = description

    def __repr__(self) -> str:
        return self.name

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "created_timestamp": self.created_timestamp,
            "owner_id": self.owner_id,
            "name": self.name,
            "code": self.code,
            "instructor": self.instructor,
            "contact_info": self.contact_info,
            "description": self.description,
        }

    def limit_query_to_owner(owner_id: int) -> Query:
        return Subject.query.filter_by(owner_id=owner_id)

    @staticmethod
    def get_subject(owner_id: int, id: int) -> List[Subject]:
        return Subject.limit_query_to_owner(owner_id).filter_by(id=id).first()

    @staticmethod
    def get_all_subjects(owner_id: int) -> list[Subject]:
        return Subject.limit_query_to_owner(owner_id).all()

    @staticmethod
    def subject_exists(owner_id: int, name: str) -> bool:
        return (
            Subject.limit_query_to_owner(owner_id).filter_by(name=name).first()
            is not None
        )

    @staticmethod
    def get_subject_by_name(owner_id: int, name: str) -> Subject:
        return Subject.limit_query_to_owner(owner_id).filter_by(name=name).first()

    @staticmethod
    def get_subject_by_code(owner_id: int, code: str) -> Subject:
        return Subject.limit_query_to_owner(owner_id).filter_by(code=code).first()
