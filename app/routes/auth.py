"""Authentication. OWNER: Emmanuel.

Done in the foundation: login, logout, role-based redirect.
TODO (Emmanuel): registration, input validation, nicer error handling.
"""
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash

from ..db import get_db

bp = Blueprint("auth", __name__)


@bp.before_app_request
def load_logged_in_user():
    """Make the current user available as g.user on every request."""
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            "SELECT id, name, email, role FROM users WHERE id = ?", (user_id,)
        ).fetchone()


def dashboard_for(user):
    if user["role"] == "lecturer":
        return url_for("lecturer.dashboard")
    return url_for("student.dashboard")


@bp.route("/")
def index():
    if g.user is None:
        return redirect(url_for("auth.login"))
    return redirect(dashboard_for(g.user))


@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        user = get_db().execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()

        if user is None or not check_password_hash(user["password_hash"], password):
            flash("Incorrect email or password.", "error")
        else:
            session.clear()
            session["user_id"] = user["id"]
            return redirect(dashboard_for(user))

    return render_template("auth/login.html")


@bp.route("/register")
def register():
    # TODO (Emmanuel): build the registration form and save the new student.
    return render_template("auth/register.html")


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
