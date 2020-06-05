import json

with open("../docs/credentials.json") as file:
    credentials = json.load(file)

SECRET_KEY = credentials.get("SECRET_KEY")
MAIL_USERNAME = credentials.get("MAIL_USERNAME")
MAIL_PASSWORD = credentials.get("MAIL_PASSWORD")
MAIL_DEFAULT_SENDER = credentials.get("MAIL_DEFAULT_SENDER")
RECIPIENTS = credentials.get("RECIPIENTS")
