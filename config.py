import os

SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-change-me")
DATABASE = os.path.join("instance", "handin.db")
UPLOAD_FOLDER = os.path.join("instance", "uploads")
