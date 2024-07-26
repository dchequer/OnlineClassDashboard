# DashboardApp/api/api.py
from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    url_for,
    session,
    flash,
    jsonify,
)
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
    json_deliverables = [
        deliverable.to_dict()
        for deliverable in Deliverable.get_all_deliverables(user_id)
    ]

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
    subject.contact_info = request.json.get("subject-contact-info")

    # save the updated subject to the database
    subject.save()

    return jsonify(subject.to_dict())


@api_bp.route("subject/delete/<subject_name>", methods=["DELETE"])
def delete_subject(subject_name: str):
    pass


@api_bp.route("meeting/update/<meeting_name>", methods=["POST"])
def update_meeting(meeting_name: str):
    # get the meeting from the database
    user_id = session.get("user_id")
    meeting = Meeting.get_meeting_by_name(user_id, meeting_name)

    print("attempting to update meeting_name: ", meeting_name)

    if meeting is None:
        return jsonify({"error": "Meeting not found"}), 404

    # update the meeting with the new data
    meeting.name = request.json.get("meeting-name")
    meeting.description = request.json.get("meeting-description")

    meeting.date = request.json.get("meeting-date")
    meeting.location = request.json.get("meeting-location")
    meeting.time = request.json.get("meeting-time")

    # save the updated meeting to the database
    meeting.save()

    return jsonify(meeting.to_dict())


@api_bp.route("meeting/delete/<meeting_name>", methods=["DELETE"])
def delete_meeting(meeting_name: str):
    pass


@api_bp.route("deliverable/update/<deliverable_title>", methods=["POST"])
def update_deliverable(deliverable_title: str):
    # get the deliverable from the database
    user_id = session.get("user_id")
    deliverable = Deliverable.get_deliverable_by_title(user_id, deliverable_title)

    print("attempting to update deliverable_title: ", deliverable_title)

    if deliverable is None:
        return jsonify({"error": "Deliverable not found"}), 404

    # update the deliverable with the new data
    deliverable.title = request.json.get("deliverable-title")
    deliverable.description = request.json.get("deliverable-description")

    deliverable.assigned_date = request.json.get("deliverable-assigned-date")
    deliverable.due_date = request.json.get("deliverable-due-date")
    deliverable.status = request.json.get("deliverable-status")
    deliverable.grade = request.json.get("deliverable-grade")

    # save the updated deliverable to the database
    deliverable.save()

    return jsonify(deliverable.to_dict())
