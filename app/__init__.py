"""HandIn application factory.

All route modules are registered here ONCE so teammates never need to edit this file.
"""
import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object("config")

    os.makedirs(app.instance_path, exist_ok=True)
    app.config["DATABASE"] = os.path.join(app.instance_path, "handin.db")
    app.config["UPLOAD_FOLDER"] = os.path.join(app.instance_path, "uploads")

    if test_config:
        app.config.update(test_config)

    from . import db
    db.init_app(app)

    from .routes import auth, student, lecturer, submission, grading
    app.register_blueprint(auth.bp)          # Emmanuel
    app.register_blueprint(student.bp)       # Emmanuel
    app.register_blueprint(submission.bp)    # Ted
    app.register_blueprint(lecturer.bp)      # Lewis
    app.register_blueprint(grading.bp)       # Elvis

    return app
