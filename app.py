from flask import Flask
from backend.config import Config
from backend.extensions import db, migrate
from backend.routes.health import health_bp
from backend.routes.contact import contact_bp


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config or Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(health_bp)
    app.register_blueprint(contact_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
