from flask import render_template

def init_app(app):
    @app.route("/")
    @app.route("/index")
    def index():
        return render_template("index.html")