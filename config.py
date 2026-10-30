import os

# Never commit real secrets. Set SECRET_KEY in the environment for anything beyond local development.
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-change-me")
