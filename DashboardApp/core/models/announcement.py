from __future__ import annotations
from datetime import datetime
from DashboardApp import db


class Announcement(db.Model):
    __tablename__ = "announcement"

    # identifiers
    id = db.Column(db.Integer, primary_key=True)
    created_timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now())

    # announcement details
    title = db.Column(db.String(32), nullable=False)
    content = db.Column(db.String(256), nullable=False)
    author = db.Column(db.String(16), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"), nullable=False)

    def __init__(self, title: str, content: str, author: str, subject_id: int):
        self.title = title
        self.content = content
        self.author = author
        self.subject_id = subject_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_announcement(announcement_id: int) -> Announcement:
        return Announcement.query.filter_by(id=announcement_id).first()

    @staticmethod
    def get_all_announcements() -> list[Announcement]:
        return Announcement.query.all()

    @staticmethod
    def get_announcements_by_subject(subject_id: int) -> list[Announcement]:
        return Announcement.query.filter_by(subject_id=subject_id).all()

    @staticmethod
    def search_announcements(search_term: str) -> list[Announcement]:
        return Announcement.query.filter(
            Announcement.title.ilike(f"%{search_term}%")
        ).all()
