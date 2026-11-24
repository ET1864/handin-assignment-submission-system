"""Lecturer course and assignment feature routes."""
from datetime import datetime

from flask import Blueprint, abort, flash, g, redirect, render_template, request, url_for

from ..auth_utils import role_required
from ..db import get_db

bp = Blueprint("lecturer", __name__, url_prefix="/lecturer")


@bp.route("/")
@role_required("lecturer")
def dashboard():
    db = get_db()
    courses = db.execute(
        """
        SELECT c.id, c.code, c.title, COUNT(DISTINCT a.id) AS assignment_count
        FROM courses c
        LEFT JOIN assignments a ON a.course_id = c.id
        WHERE c.lecturer_id = ?
        GROUP BY c.id
        ORDER BY c.code
        """,
        (g.user["id"],),
    ).fetchall()
    assignments = db.execute(
        """
        SELECT a.id, a.title, a.deadline, c.code AS course_code,
               COUNT(s.id) AS submission_count,
               COUNT(s.grade) AS graded_count
        FROM assignments a
        JOIN courses c ON c.id = a.course_id
        LEFT JOIN submissions s ON s.assignment_id = a.id
        WHERE c.lecturer_id = ?
        GROUP BY a.id
        ORDER BY a.deadline, a.title
        """,
        (g.user["id"],),
    ).fetchall()
    return render_template(
        "lecturer/dashboard.html", courses=courses, assignments=assignments
    )


@bp.route("/assignments/new", methods=("GET", "POST"))
@role_required("lecturer")
def create_assignment():
    db = get_db()
    courses = db.execute(
        "SELECT id, code, title FROM courses WHERE lecturer_id = ? ORDER BY code",
        (g.user["id"],),
    ).fetchall()
    form = request.form if request.method == "POST" else {}

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        course_id = request.form.get("course_id", "")
        deadline_input = request.form.get("deadline", "")

        if not title:
            flash("Enter an assignment title.", "error")
        else:
            course = db.execute(
                "SELECT id FROM courses WHERE id = ? AND lecturer_id = ?",
                (course_id, g.user["id"]),
            ).fetchone()
            if course is None:
                flash("Choose one of your courses.", "error")
            else:
                try:
                    deadline = datetime.strptime(
                        deadline_input, "%Y-%m-%dT%H:%M"
                    ).strftime("%Y-%m-%d %H:%M")
                except ValueError:
                    flash("Enter a valid deadline.", "error")
                else:
                    db.execute(
                        """INSERT INTO assignments (course_id, title, description, deadline)
                           VALUES (?, ?, ?, ?)""",
                        (course["id"], title, description, deadline),
                    )
                    db.commit()
                    flash("Assignment created.", "info")
                    return redirect(url_for("lecturer.dashboard"))

        return render_template(
            "lecturer/assignment_form.html", courses=courses, form=form
        )

    return render_template(
        "lecturer/assignment_form.html", courses=courses, form=form
    )


@bp.route("/assignments/<int:assignment_id>/submissions")
@role_required("lecturer")
def assignment_submissions(assignment_id):
    db = get_db()
    assignment = db.execute(
        """
        SELECT a.id, a.title, a.description, a.deadline, c.code AS course_code,
               c.title AS course_title, c.id AS course_id
        FROM assignments a
        JOIN courses c ON c.id = a.course_id
        WHERE a.id = ? AND c.lecturer_id = ?
        """,
        (assignment_id, g.user["id"]),
    ).fetchone()
    if assignment is None:
        abort(404)

    students = db.execute(
        """
        SELECT u.name, u.email, s.id AS submission_id, s.content, s.file_path,
               s.submitted_at, s.grade, s.feedback
        FROM enrollments e
        JOIN users u ON u.id = e.student_id
        LEFT JOIN submissions s
          ON s.assignment_id = ? AND s.student_id = e.student_id
        WHERE e.course_id = ?
        ORDER BY u.name
        """,
        (assignment_id, assignment["course_id"]),
    ).fetchall()
    return render_template(
        "lecturer/submissions.html", assignment=assignment, students=students
    )
