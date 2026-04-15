from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_module2_demo_index_renders() -> None:
    response = client.get("/demo/module2")
    assert response.status_code == 200
    text = response.text
    assert "Module 2 Demo Index" in text
    assert "/demo/profile-ui" in text
    assert "m2-main-case-start" in text
    assert "m2-style-bad-patch" in text
