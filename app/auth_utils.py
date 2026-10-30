"""Access-control decorators. Use them on any route that needs a logged-in user.

    @bp.route("/something")
    @role_required("student")
    def something(): ...
"""
from functools import wraps

from flask import abort, flash, g, redirect, url_for


def login_required(view):
    @wraps(view)
    def wrapped(**kwargs):
        if g.user is None:
            flash("Please log in to continue.", "info")
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped


def role_required(role):
    """Allow only users with the given role ('student' or 'lecturer')."""
    def decorator(view):
        @wraps(view)
        def wrapped(**kwargs):
            if g.user is None:
                flash("Please log in to continue.", "info")
                return redirect(url_for("auth.login"))
            if g.user["role"] != role:
                abort(403)
            return view(**kwargs)
        return wrapped
    return decorator
