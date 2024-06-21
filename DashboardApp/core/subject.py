from flask import render_template, Blueprint, request, session
from flask_login import login_required
from .models.subject import Subject


subject_bp = Blueprint('subject', __name__, static_folder='static', template_folder='templates')


def get_subjects():
    owner_id = session["user_id"]
    subjects = Subject.get_all_subjects(owner_id=owner_id)
    print(subjects)
    print(owner_id)

    return subjects

@subject_bp.route('/subjects', methods=['GET', 'POST'])
@login_required
def subjects():
    if request.method == 'POST':
        owner_id = session['user_id']
        subject_name = request.form['name']
        subject_code = request.form['code']
        instructor = request.form['instructor']
        contact_info = request.form['contact-info']
        description = request.form['description']

        print(f"Received new subject request: {owner_id=}, {subject_name=}, {subject_code=}, {instructor=}, {contact_info=}, {description=}")
        print("Checking if subject already exists...")
        if not Subject.subject_exists(owner_id, subject_name):
            print("Subject does not exist. Creating new subject...")
            subject = Subject(owner_id, subject_name, subject_code, instructor, contact_info, description)
            subject.save()
        else:
            print("Subject already exists")
            return render_template('subjects.html', error="Subject already exists")

    return render_template('subjects.html', subjects=get_subjects())

