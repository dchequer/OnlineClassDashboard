# DashboardApp/__init__.py
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    # init database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
    db.init_app(app)

    # import models
    from DashboardApp.auth.models import User
    
    # create tables and models
    with app.app_context():
        db.create_all()

    # import blueprints
    from DashboardApp.auth import auth
    app.register_blueprint(auth.auth_bp, url_prefix='/auth')

    # redirect to /auth/login
    @app.route('/')
    def home():
        return redirect(url_for('auth.login'))
    
    return app