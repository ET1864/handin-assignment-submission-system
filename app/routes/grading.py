"""Viewing and grading a single submission. OWNER: Elvis"""

from flask import Blueprint, render_template
from app.auth_utils import login_required, role_required

bp = Blueprint("grading", __name__, url_prefix="/grading")


@bp.route("/assignment/<int:assignment_id>/submissions")
@login_required
@role_required("lecturer")
def submissions(assignment_id):
    return render_template("grading/submissions.html")