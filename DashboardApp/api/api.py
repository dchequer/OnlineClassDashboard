# DashboardApp/api/api.py
from flask import Blueprint, redirect, render_template, request, url_for, session, flash, jsonify
from ..core.models.subject import Subject
from ..core.models.deliverable import Deliverable
from ..core.models.meeting import Meeting

api_bp = Blueprint(
    "api", __name__
)

@api_bp.route("user/id", methods=["GET"])
def get_user_id() -> str:
    return jsonify(session.get("user_id"))

@api_bp.route("subjects/user_id=<user_id>", methods=["GET"])
def get_user_subjects(user_id: int = None) -> list[Subject]:
    if user_id is None: user_id = session.get("user_id")

    # get the subjects for the user    
    json_subjects = [subject.to_dict() for subject in Subject.get_all_subjects(user_id)]

    return json_subjects

@api_bp.route("deliverables/user_id=<user_id>", methods=["GET"])
def get_user_deliverables(user_id:int = None) -> list[Deliverable]:
    if user_id is None: user_id = session.get("user_id")

    # get the deliverables for the user
    json_deliverables = [deliverable.to_dict() for deliverable in Deliverable.get_all_deliverables(user_id)]

    return json_deliverables

@api_bp.route("meetings/user_id=<user_id>", methods=["GET"])
def get_user_meetings(user_id:int = None) -> list[Meeting]:
    if user_id is None: user_id = session.get("user_id")

    # get the meeetings for the user
    json_meetings = [meeting.to_dict() for meeting in Meeting.get_all_meetings(user_id)]

    return json_meetings