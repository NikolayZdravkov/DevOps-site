import os
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/devops_site"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class ContactMessage(db.Model):
    __tablename__ = "contact_messages"

    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(120), nullable=False)
    email      = db.Column(db.String(254), nullable=False)
    message    = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "timestamp": datetime.utcnow().isoformat()})


@app.route("/api/db-health")
def db_health():
    try:
        db.session.execute(db.text("SELECT 1"))
        return jsonify({"status": "ok", "database": "connected"})
    except Exception as e:
        return jsonify({"status": "error", "database": str(e)}), 500


@app.route("/api/contact", methods=["POST"])
def contact():
    data = request.get_json()
    if not data or not data.get("name") or not data.get("email"):
        return jsonify({"error": "name and email are required"}), 400

    msg = ContactMessage(
        name=data["name"],
        email=data["email"],
        message=data.get("message", ""),
    )
    db.session.add(msg)
    db.session.commit()

    return jsonify({"message": f"Thanks {data['name']}, we'll be in touch!"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
