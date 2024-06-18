from flask import render_template, Blueprint, request, session
from .models.subject import Subject


deliverable_bp = Blueprint('deliverable', __name__, static_folder='static', template_folder='templates')


def get_deliverables():
    owner_id = session["user_id"]
    subjects = Subject.get_all_subjects(owner_id=owner_id)

    return subjects

@deliverable_bp.route('/deliverables', methods=['GET', 'POST'])
def deliverables():
    if request.method == 'POST':
       pass

    deliverables = get_deliverables()
    return render_template('deliverables.html', deliverables=deliverables)

