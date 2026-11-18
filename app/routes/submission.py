"""Student submission pages. OWNER: Ted."""
from datetime import datetime

from flask import Blueprint, abort, g, render_template

from ..auth_utils import role_required
from ..db import get_db

bp = Blueprint("submission", __name__, url_prefix="/submissions")


@bp.route("/class/<int:course_id>")
@role_required("student")
def class_page(course_id):
    db = get_db()

    # Only show the class if this student is enrolled in it.
    course = db.execute(
        """
        SELECT c.id, c.code, c.title
        FROM courses c
        JOIN enrollments e ON e.course_id = c.id
        WHERE c.id = ? AND e.student_id = ?
        """,
        (course_id, g.user["id"]),
    ).fetchone()
    if course is None:
        abort(404)

    # One row per assignment. If the student has no submission, the
    # submission columns come back empty (that is what LEFT JOIN does).
    rows = db.execute(
        """
        SELECT a.id, a.title, a.deadline, s.submitted_at, s.grade
        FROM assignments a
        LEFT JOIN submissions s
               ON s.assignment_id = a.id AND s.student_id = ?
        WHERE a.course_id = ?
        ORDER BY a.deadline
        """,
        (g.user["id"], course_id),
    ).fetchall()

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    pending = [r for r in rows if r["submitted_at"] is None]
    submitted = [r for r in rows if r["submitted_at"] is not None]
    return render_template("student/class.html", course=course,
                           pending=pending, submitted=submitted, now=now)
@bp.route("/assignment/<int:assignment_id>")
@role_required("student")
def assignment_page(assignment_id):
    db = get_db()

    # Fetch the assignment only if the student is enrolled in its course.
    assignment = db.execute(
        """
        SELECT a.id, a.title, a.description, a.deadline,
               c.id AS course_id, c.code
        FROM assignments a
        JOIN courses c ON c.id = a.course_id
        JOIN enrollments e ON e.course_id = c.id
        WHERE a.id = ? AND e.student_id = ?
        """,
        (assignment_id, g.user["id"]),
    ).fetchone()
    if assignment is None:
        abort(404)

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    return render_template("student/assignment.html",
                           assignment=assignment, now=now)