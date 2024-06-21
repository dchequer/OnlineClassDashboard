# DashboardApp/auth/models/user.py
from __future__ import annotations
from datetime import datetime
from DashboardApp import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    created_timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now())
    username = db.Column(db.String(16), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)
    last_login = db.Column(db.DateTime, nullable=True, default=datetime.now())
    last_logout = db.Column(db.DateTime, nullable=True, default=None)

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def __repr__(self) -> str:
        return f"<User {self.username}>"

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def login(self) -> None:
        self.last_login = datetime.now()
        db.session.commit()

    def logout(self) -> None:
        self.last_logout = datetime.now()
        db.session.commit()

    def get(self, args: str) -> list:
        return [getattr(self, arg.strip()) for arg in args.split(",")]


    # - - - Flask Login methods - - - #
    def is_authenticated(self):
        print("mine")
        return True
    
    def is_anonymous(self):
        return False
    
    def is_active(self):
        return True
    
    def get_id(self):
        return str(self.id)
    # - - - - - - - - - - - - - - - - #

    @staticmethod
    def user_exists(username) -> bool:
        return User.query.filter_by(username=username).first() is not None

    @staticmethod
    def authenticate(username, password) -> User | None:
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            return user
        return None

    @staticmethod
    def get_timestamp(id) -> datetime | None:
        user = User.query.filter_by(id=id).first()
        if user is not None:
            return user.created_timestamp
        else:
            return None

    @staticmethod
    def get_user(id) -> User | None:
        return User.query.filter_by(id=id).first()
