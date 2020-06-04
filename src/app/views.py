from flask import render_template
from app.email import email as email_blueprint


def init_app(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    app.register_blueprint(email_blueprint)
