from fastapi.testclient import TestClient

from app import db
from app.main import app

client = TestClient(app)


def test_health_reports_database_ok(monkeypatch):
    monkeypatch.setattr(db, "database_is_reachable", lambda: True)

    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "database": "ok"}


def test_health_reports_database_unavailable(monkeypatch):
    monkeypatch.setattr(db, "database_is_reachable", lambda: False)

    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "database": "unavailable"}
