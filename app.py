from flask import Flask
from backend.config import Config
from backend.extensions import db
from backend.routes.health import health_bp
from backend.routes.contact import contact_bp


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config or Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(health_bp)
    app.register_blueprint(contact_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
