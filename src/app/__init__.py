from flask import Flask

def create_app():
    app = Flask(__name__, static_folder="static")
    from app import views
    views.init_app(app)

    return app