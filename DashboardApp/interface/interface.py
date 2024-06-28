# interface/interface.py
from flask import Blueprint, redirect, render_template, request, url_for, session
from flask_login import login_required
from ..core.models.subject import Subject
from ..core.models.meeting import Meeting
from ..core.models.deliverable import Deliverable

interface_bp = Blueprint("interface", __name__, static_folder="static", template_folder="templates")


@interface_bp.route("/subject/<string:subject_name>", methods=["GET"])
@login_required
def subject(subject_name: str):
    user_id = session["user_id"]
    subject = Subject.get_subject_by_name(owner_id=user_id, name=subject_name)

    return render_template("subject.html", subject=subject)


@interface_bp.route("/meeting/<string:meeting_name>", methods=["GET"])
@login_required
def meeting(meeting_name: str):
    user_id = session["user_id"]
    meeting = Meeting.get_meeting_by_name(owner_id=user_id, name=meeting_name)
    meeting.subject_name = Subject.get_subject(owner_id=user_id, id=meeting.subject_id).name

    return render_template("meeting.html", meeting=meeting)


@interface_bp.route("/deliverable/<string:deliverable_title>", methods=["GET"])
@login_required
def deliverable(deliverable_title: str):
    user_id = session["user_id"]
    deliverable = Deliverable.get_deliverable_by_title(owner_id=user_id, title=deliverable_title)
    try:
        deliverable.subject_name = Subject.get_subject(owner_id=user_id, id=deliverable.subject_id).name
    except AttributeError:
        deliverable.subject_name = None
    try:
        deliverable.meeting_name = Meeting.get_meeting(owner_id=user_id, id=deliverable.meeting_id).name
    except AttributeError:
        deliverable.meeting_name = None

    print(deliverable)

    return render_template("deliverable.html", deliverable=deliverable)
