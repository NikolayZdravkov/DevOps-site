from flask import Blueprint, jsonify, request
from backend.extensions import db
from backend.models import ContactMessage

contact_bp = Blueprint("contact", __name__)


@contact_bp.route("/api/contact", methods=["POST"])
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
