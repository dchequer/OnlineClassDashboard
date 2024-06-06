# home/home.py
from flask import render_template
from flask_login import login_required, current_user

@app.route('/')
@login_required
def home():
    return render_template('home.html', name=current_user.name)