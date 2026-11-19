"""Viewing and grading submissions. OWNER: Elvis"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.db import get_db
from app.auth_utils import login_required, role_required

bp = Blueprint("grading", __name__, url_prefix="/grading")


@bp.route("/assignment/<int:assignment_id>/submissions")
@login_required
@role_required("lecturer")
def submissions(assignment_id):
    db = get_db()
    
    # Query assignment details
    assignment = db.execute(
        'SELECT * FROM assignments WHERE id = ?', (assignment_id,)
    ).fetchone()

    # Query all students enrolled in the course along with their submission status/grade
    submissions_list = db.execute(
        '''
        SELECT u.id as student_id, u.name as student_name, u.reg_no as student_reg,
               s.id as submission_id, s.submitted_at, s.grade
        FROM enrollments e
        JOIN users u ON e.student_id = u.id
        LEFT JOIN submissions s ON s.student_id = u.id AND s.assignment_id = ?
        WHERE e.course_id = (SELECT course_id FROM assignments WHERE id = ?)
        ''',
        (assignment_id, assignment_id)
    ).fetchall()

    return render_template(
        "grading/submissions.html",
        assignment=assignment,
        submissions=submissions_list
    )


@bp.route('/submission/<int:submission_id>/grade', methods=['GET', 'POST'])
@login_required
@role_required("lecturer")
def grade_submission(submission_id):
    db = get_db()
    
    if request.method == 'POST':
        grade = request.form.get('grade')
        feedback = request.form.get('feedback')
        
        db.execute(
            'UPDATE submissions SET grade = ?, feedback = ? WHERE id = ?',
            (grade, feedback, submission_id)
        )
        db.commit()
        
        flash('Grade updated successfully!', 'success')
        
        submission = db.execute(
            'SELECT assignment_id FROM submissions WHERE id = ?', (submission_id,)
        ).fetchone()
        
        return redirect(url_for('grading.submissions', assignment_id=submission['assignment_id']))

    submission = db.execute(
        '''
        SELECT s.id, s.assignment_id, s.submitted_at, s.content, s.grade, s.feedback,
               u.name as student_name, u.reg_no as student_reg
        FROM submissions s
        JOIN users u ON s.student_id = u.id
        WHERE s.id = ?
        ''',
        (submission_id,)
    ).fetchone()

    return render_template('grading/grade.html', submission=submission)