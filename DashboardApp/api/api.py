# DashboardApp/api/api.py
from flask import Blueprint, redirect, render_template, request, url_for, session, flash, jsonify
from ..core.models.subject import Subject
from ..core.models.deliverable import Deliverable
from ..core.models.meeting import Meeting

api_bp = Blueprint("api", __name__)


@api_bp.route("user/id", methods=["GET"])
def get_user_id() -> str:
    return jsonify(session.get("user_id"))


@api_bp.route("subjects/user_id=<user_id>", methods=["GET"])
def get_user_subjects(user_id: int = None) -> list[Subject]:
    if user_id is None:
        user_id = session.get("user_id")

    # get the subjects for the user
    json_subjects = [subject.to_dict() for subject in Subject.get_all_subjects(user_id)]

    return json_subjects


@api_bp.route("deliverables/user_id=<user_id>", methods=["GET"])
def get_user_deliverables(user_id: int = None) -> list[Deliverable]:
    if user_id is None:
        user_id = session.get("user_id")

    # get the deliverables for the user
    json_deliverables = [deliverable.to_dict() for deliverable in Deliverable.get_all_deliverables(user_id)]

    return json_deliverables


@api_bp.route("meetings/user_id=<user_id>", methods=["GET"])
def get_user_meetings(user_id: int = None) -> list[Meeting]:
    if user_id is None:
        user_id = session.get("user_id")

    # get the meeetings for the user
    json_meetings = [meeting.to_dict() for meeting in Meeting.get_all_meetings(user_id)]

    return json_meetings


@api_bp.route("subject/update/<subject_name>", methods=["POST"])
def update_subject(subject_name: str):
    # get the subject from the database
    user_id = session.get("user_id")
    subject = Subject.get_subject_by_name(user_id, subject_name)

    print("attempting to update subject_name: ", subject_name)

    if subject is None:
        return jsonify({"error": "Subject not found"}), 404

    # update the subject with the new data
    subject.name = request.json.get("subject-name")
    subject.code = request.json.get("subject-code")
    subject.description = request.json.get("subject-description")

    subject.instructor = request.json.get("subject-instructor")
    subject.contact = request.json.get("subject-contact")

    # save the updated subject to the database
    subject.save()

    return jsonify(subject.to_dict())
