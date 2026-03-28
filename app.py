from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "timestamp": datetime.utcnow().isoformat()})


@app.route("/api/contact", methods=["POST"])
def contact():
    from flask import request
    data = request.get_json()
    if not data or not data.get("name") or not data.get("email"):
        return jsonify({"error": "name and email are required"}), 400
    # Placeholder — wire up email/DB as needed
    return jsonify({"message": f"Thanks {data['name']}, we'll be in touch!"})


if __name__ == "__main__":
    app.run(debug=True)
