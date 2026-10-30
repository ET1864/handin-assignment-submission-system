"""Lecturer pages. OWNER: Lewis.

Planned: my classes, create assignment, assignment list, who-submitted view.
Copy the pattern in student.py (query with get_db(), render a template).
"""
from flask import Blueprint, render_template

from ..auth_utils import role_required

bp = Blueprint("lecturer", __name__, url_prefix="/lecturer")


@bp.route("/")
@role_required("lecturer")
def dashboard():
    # TODO (Lewis): list the courses this lecturer teaches.
    return render_template("lecturer/dashboard.html")
