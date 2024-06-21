# home/home.py
from flask import Blueprint, redirect, render_template, request, url_for, session
from flask_login import login_required
from ..auth.models.user import User

core_bp = Blueprint(
    "core", __name__, static_folder="static", template_folder="templates"
)


@core_bp.route("/home")
@login_required
def home():
    # check if the user is logged in
    if "user_id" not in session:

        return redirect(url_for("auth.login"))

    # else
    user = User.get_user(session["user_id"])

    # get the user's info
    username, user_id, created_timestamp = user.get("username, id, created_timestamp")
    return render_template(
        "home.html", username=username, created_timestamp=created_timestamp
    )
