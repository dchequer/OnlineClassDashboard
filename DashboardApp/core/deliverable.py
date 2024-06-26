from flask import render_template, Blueprint, request, session, redirect, url_for
from flask_login import login_required
from .models.subject import Subject
from .models.deliverable import Deliverable
from datetime import date


deliverable_bp = Blueprint("deliverable", __name__, static_folder="static", template_folder="templates")


def get_deliverables():
    owner_id = session["user_id"]
    deliverables = Deliverable.get_all_deliverables(owner_id=owner_id)
    return deliverables


def extract_date(date_string):
    year, month, day = date_string.split("-")
    assigned_date = date(int(year), int(month), int(day))
    return assigned_date


@deliverable_bp.route("/deliverables", methods=["GET", "POST"])
@login_required
def deliverables():
    if request.method == "POST":
        owner_id = session["user_id"]
        title = request.form["title"]
        assigned_date = extract_date(request.form["assigned-date"])
        due_date = extract_date(request.form["due-date"])
        description = request.form["description"]

        subject_id = request.form["subject"] if request.form["subject"] != "0" else None
        meeting_id = request.form["meeting"] if request.form["meeting"] != "0" else None

        print(f"Received new deliverable request: {owner_id=}, {title=}, {assigned_date=}, {due_date=}, {subject_id=}, {meeting_id=}, {description=}")
        print("Checking if deliverable already exists...")
        if not Deliverable.deliverable_exists(owner_id, title):
            print("Deliverable does not exist. Creating new deliverable...")
            deliverable = Deliverable(
                owner_id,
                title,
                description,
                assigned_date,
                due_date,
                subject_id,
                meeting_id,
            )
            deliverable.save()
        else:
            print("Deliverable already exists")
            return render_template("deliverables.html", error="Deliverable already exists")

    deliverables = get_deliverables()
    return render_template("deliverables.html", deliverables=deliverables)


@deliverable_bp.route("/deliverables/<string:deliverable_title>", methods=["GET"])
@login_required
def deliverable(deliverable_title: str):
    return redirect(url_for("interface.deliverable", deliverable_title=deliverable_title))
