import os

SECRET_KEY = os.environ.get("SECRET_KEY")
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER")
RECIPIENTS = os.environ.get("RECIPIENTS")
