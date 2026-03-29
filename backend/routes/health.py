from datetime import datetime
from flask import Blueprint, jsonify
from backend.extensions import db

health_bp = Blueprint("health", __name__)


@health_bp.route("/api/health")
def health():
    return jsonify({"status": "ok", "timestamp": datetime.utcnow().isoformat()})


@health_bp.route("/api/db-health")
def db_health():
    try:
        db.session.execute(db.text("SELECT 1"))
        return jsonify({"status": "ok", "database": "connected"})
    except Exception as e:
        return jsonify({"status": "error", "database": str(e)}), 500
