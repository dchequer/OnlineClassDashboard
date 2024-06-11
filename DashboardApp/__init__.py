# DashboardApp/__init__.py
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.secret_key = 'secret_key'

    # init database engine
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
    db.init_app(app)

    # init migration engine
    migrate.init_app(app, db)

    # import models
    from DashboardApp.auth.models.user import User
    
    # create tables and models
    with app.app_context():
        #db.drop_all()
        db.create_all()

    # import blueprints
    from DashboardApp.auth import auth
    app.register_blueprint(auth.auth_bp, url_prefix='/auth')
    from DashboardApp.core import core
    app.register_blueprint(core.core_bp, url_prefix='/core')

    # redirect to /auth/login
    @app.route('/')
    def core():
        return redirect(url_for('auth.login'))
    
    return app