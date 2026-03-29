import pytest
from unittest.mock import patch
from app import create_app
from backend.extensions import db


class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


@pytest.fixture
def client():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()


def test_health(client):
    res = client.get("/api/health")
    assert res.status_code == 200
    data = res.get_json()
    assert data["status"] == "ok"
    assert "timestamp" in data


def test_db_health_connected(client):
    res = client.get("/api/db-health")
    assert res.status_code == 200
    data = res.get_json()
    assert data["status"] == "ok"
    assert data["database"] == "connected"


def test_db_health_error(client):
    with patch("backend.routes.health.db.session.execute", side_effect=Exception("DB down")):
        res = client.get("/api/db-health")
        assert res.status_code == 500
        data = res.get_json()
        assert data["status"] == "error"
        assert "DB down" in data["database"]


def test_contact_success(client):
    res = client.post("/api/contact", json={
        "name": "Alice",
        "email": "alice@example.com",
        "message": "Hello!"
    })
    assert res.status_code == 200
    data = res.get_json()
    assert "Alice" in data["message"]


def test_contact_missing_name(client):
    res = client.post("/api/contact", json={"email": "alice@example.com"})
    assert res.status_code == 400
    assert "required" in res.get_json()["error"]


def test_contact_missing_email(client):
    res = client.post("/api/contact", json={"name": "Alice"})
    assert res.status_code == 400
    assert "required" in res.get_json()["error"]


def test_contact_empty_body(client):
    res = client.post("/api/contact", json={})
    assert res.status_code == 400
