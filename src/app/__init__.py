from flask import Flask
from flask_mail import Mail

from app.credentials import MAIL_PASSWORD, MAIL_USERNAME, SECRET_KEY
from app.filters import render_json

mail = Mail()


def create_app():
    app = Flask(__name__, static_folder="static")
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USE_SSL"] = True
    app.config["MAIL_USERNAME"] = MAIL_USERNAME
    app.config["MAIL_PASSWORD"] = MAIL_PASSWORD
    app.jinja_env.filters["render_json"] = render_json

    mail.init_app(app)

    from app import views
    views.init_app(app)

    return app
