# DashboardApp/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .auth import auth
from .auth.models import user

db:SQLAlchemy = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # init database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db'
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # blueprints
    app.register_blueprint(auth.auth_bp)

    return app