from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "DevOps Capstone API is running"

def test_info():
    response = client.get("/info")

    assert response.status_code == 200
    assert response.json()["application"] == "DevOps Demo API"
    assert response.json()["environment"] == "development"
    assert response.json()["version"] == "1.0.0"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_users():
    response = client.get("/users")

    assert response.status_code == 200

    users = response.json()

    assert len(users) == 2