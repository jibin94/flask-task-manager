from flask import Flask
from .extensions import db
from .routes.html_routes import html_bp
from .routes.api_routes import api_bp

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Register blueprints
    app.register_blueprint(html_bp)
    app.register_blueprint(api_bp)

    with app.app_context():
        db.create_all()

    return app
