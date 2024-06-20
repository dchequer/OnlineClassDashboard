# core/meeting.py
from flask import Blueprint, redirect, render_template, request, url_for, session
from .models.meeting import Meeting
from datetime import date

meeting_bp = Blueprint(
    "meeting", __name__, static_folder="static", template_folder="templates"
)

def get_meetings():
    owner_id = session["user_id"]
    meetings = Meeting.get_all_meetings(owner_id)
    print(owner_id)
    print(meetings)

    return meetings

def extract_date(date_string):
    year, month, day = date_string.split("-")
    assigned_date = date(int(year), int(month), int(day))
    return assigned_date

@meeting_bp.route("/meetings", methods=["GET", "POST"])
def meetings():
    if request.method == "POST":
        owner_id = session["user_id"]
        name = request.form["name"]
        date = extract_date(request.form["date"])
        location = request.form["location"]
        description = request.form["description"]

        subject_id = request.form["subject"] if request.form["subject"]!="0" else None

        print(
            f"Received new meeting request: {owner_id=}, {name=}, {date=}, {subject_id=}, {description=}"
        )
        print("Checking if meeting already exists...")
        if not Meeting.meeting_exists(owner_id, name):
            print("Deliverable does not exist. Creating new deliverable...")
            meeting = Meeting(
                owner_id,
                name,
                subject_id,
                date,
                location,
                description
            )
            meeting.save()
        else:
            print("Deliverable already exists")
            return render_template(
                "deliverables.html", error="Deliverable already exists"
            )

    return render_template("meetings.html", meetings=get_meetings())
    
