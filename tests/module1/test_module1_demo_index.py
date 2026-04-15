from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_module1_demo_index_page() -> None:
    response = client.get("/demo/module1")
    assert response.status_code == 200
    body = response.text
    assert "Module 1 Demo Index" in body
    assert "/demo/profile-ui" in body
