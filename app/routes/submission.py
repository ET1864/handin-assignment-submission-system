"""Student submission pages. OWNER: Ted."""
from flask import Blueprint, render_template

from ..auth_utils import role_required

bp = Blueprint("submission", __name__, url_prefix="/submissions")


@bp.route("/class/<int:course_id>")
@role_required("student")
def class_page(course_id):
    # Static layout only for now. No database query yet.
    return render_template("student/class.html")