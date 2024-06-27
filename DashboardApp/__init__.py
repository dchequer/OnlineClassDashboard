# DashboardApp/__init__.py
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from dotenv import load_dotenv
import os
import config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    # load environment variables
    load_dotenv()

    # init app and configs
    app = Flask(__name__, static_url_path="/static", static_folder="static")

    app.secret_key = os.getenv("SECRET_KEY", "secret_key")

    # init database engine
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", os.getenv("SQLALCHEMY_DATABASE_URI"))
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    db.init_app(app)

    # init migration engine
    migrate.init_app(app, db)

    # init login manager
    login_manager.init_app(app)
    # login_manager.login_view = "auth.user.login"

    # import models
    from DashboardApp.auth.models.user import User
    from DashboardApp.core.models.announcement import Announcement
    from DashboardApp.core.models.deliverable import Deliverable
    from DashboardApp.core.models.meeting import Meeting
    from DashboardApp.core.models.subject import Subject

    # create tables and models
    with app.app_context():
        # db.drop_all()
        db.create_all()

    # import blueprints
    from DashboardApp.auth import auth

    app.register_blueprint(auth.auth_bp, url_prefix="/auth")

    from DashboardApp.core import core

    app.register_blueprint(core.core_bp, url_prefix="/core")

    from DashboardApp.core import deliverable

    app.register_blueprint(deliverable.deliverable_bp, url_prefix="/core")

    from DashboardApp.core import meeting

    app.register_blueprint(meeting.meeting_bp, url_prefix="/core")

    from DashboardApp.core import subject

    app.register_blueprint(subject.subject_bp, url_prefix="/core")

    from DashboardApp.api import api

    app.register_blueprint(api.api_bp, url_prefix="/api")

    from DashboardApp.interface import interface

    app.register_blueprint(interface.interface_bp, url_prefix="/interface")

    # redirect to /auth/login
    @app.route("/")
    def core():
        return redirect(url_for("auth.login"))

    return app
