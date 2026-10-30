"""Student dashboard. OWNER: Emmanuel.

This file is the PATTERN for every page in the project:
  1. protect the route with @role_required
  2. query the database with get_db()
  3. pass the rows to a template
"""
from flask import Blueprint, g, render_template

from ..auth_utils import role_required
from ..db import get_db

bp = Blueprint("student", __name__, url_prefix="/student")


@bp.route("/")
@role_required("student")
def dashboard():
    courses = get_db().execute(
        """
        SELECT c.id, c.code, c.title, u.name AS lecturer
        FROM courses c
        JOIN enrollments e ON e.course_id = c.id
        JOIN users u ON u.id = c.lecturer_id
        WHERE e.student_id = ?
        ORDER BY c.code
        """,
        (g.user["id"],),
    ).fetchall()
    return render_template("student/dashboard.html", courses=courses)
