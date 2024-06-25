# interface/interface.py
from flask import Blueprint, redirect, render_template, request, url_for, session
from flask_login import login_required
from ..core.models.subject import Subject

interface_bp = Blueprint(
    "interface", __name__, static_folder="static", template_folder="templates"
)


@interface_bp.route("/subject/<string:subject_name>", methods=["GET"])
@login_required
def subject(subject_name):
    user_id = session["user_id"]
    subject = Subject.get_subject_by_name(owner_id=user_id, subject_name=subject_name)

    return render_template("subject.html", subject=subject)
