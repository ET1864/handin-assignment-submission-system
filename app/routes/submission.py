"""Student submission pages. OWNER: Ted.

Planned: class page with pending work, submit assignment, submission status.
Use @role_required("student") and the pattern in student.py.
"""
from flask import Blueprint

bp = Blueprint("submission", __name__, url_prefix="/submissions")

# TODO (Ted): add routes here.
