from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_module3_demo_index_renders() -> None:
    response = client.get("/demo/module3")
    assert response.status_code == 200
    text = response.text
    assert "Module 3 Demo Index" in text
    assert "template pack" in text.lower()
    assert "AI can do / cannot outsource" in text
    assert "/demo/module2" in text
