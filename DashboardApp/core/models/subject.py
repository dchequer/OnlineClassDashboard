from __future__ import annotations
from datetime import datetime
from DashboardApp import db
from typing import List


class Subject(db.Model):
    __tablename__ = "subject"

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
    announcements = db.relationship("Announcement", backref="subject", lazy=True)
    deliverables = db.relationship("Deliverable", backref="subject", lazy=True)
    meetings = db.relationship("Meeting", backref="subject", lazy=True)

    def __init__(self, name: str, code: str, instructor: str, contact_info: str, description: str = None):
        self.name = name
        self.code = code
        self.instructor = instructor
        self.contact_info = contact_info
        self.description = description
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_subject(subject_id: int) -> List[Subject]:
        return Subject.query.filter_by(id=subject_id).first()
    
    @staticmethod
    def get_all_subjects() -> list[Subject]:
        return Subject.query.all()
    
    @staticmethod
    def subject_exists(subject_name: str) -> bool:
        return Subject.query.filter_by(name=subject_name).first() is not None
    
    @staticmethod
    def get_subject_by_name(subject_name: str) -> Subject:
        return Subject.query.filter_by(name=subject_name).first()
    
    @staticmethod
    def get_subject_by_code(subject_code: str) -> Subject:
        return Subject.query.filter_by(code=subject_code).first()
    
    