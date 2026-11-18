"""Student submission pages. OWNER: Ted."""
import os
from datetime import datetime

from flask import (Blueprint, abort, current_app, flash, g, redirect,
                   render_template, request, send_from_directory, url_for)
from werkzeug.utils import secure_filename

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


@bp.route("/assignment/<int:assignment_id>", methods=["GET", "POST"])
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

    # This student's submission for this assignment, if there is one.
    submission = db.execute(
        "SELECT id, file_path, submitted_at FROM submissions "
        "WHERE assignment_id = ? AND student_id = ?",
        (assignment_id, g.user["id"]),
    ).fetchone()

    if request.method == "POST":
        file = request.files.get("submission_file")
        if submission is not None:
            flash("You have already submitted this assignment.", "error")
        elif assignment["deadline"] < now:
            flash("The deadline has passed, so submissions are closed.", "error")
        elif file is None or file.filename == "":
            flash("Please choose a file to upload.", "error")
        else:
            # Save the file, then record who submitted it and when.
            filename = f"{g.user['id']}_{assignment_id}_{secure_filename(file.filename)}"
            os.makedirs(current_app.config["UPLOAD_FOLDER"], exist_ok=True)
            file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
            db.execute(
                "INSERT INTO submissions (assignment_id, student_id, file_path, submitted_at) "
                "VALUES (?, ?, ?, ?)",
                (assignment_id, g.user["id"], filename, now),
            )
            db.commit()
            flash("Submission successful.", "success")
        return redirect(url_for("submission.assignment_page",
                                assignment_id=assignment_id))

    return render_template("student/assignment.html", assignment=assignment,
                           submission=submission, now=now)
