from flask import Flask
from flask_mail import Mail

mail = Mail()


def create_app():
    app = Flask(__name__, static_folder="static")
    app.config["SECRET_KEY"] = "DontTellAnyone"
    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USE_SSL"] = True
    app.config["MAIL_DEBUG"] = True
    app.config["MAIL_USERNAME"] = "danbailotest"
    app.config["MAIL_PASSWORD"] = "mystrongpassword"
    app.config["MAIL_DEFAULT_SENDER"] = 'YOU <danbailotest@gmail.com>'

    mail.init_app(app)

    from app import views
    views.init_app(app)

    return app
