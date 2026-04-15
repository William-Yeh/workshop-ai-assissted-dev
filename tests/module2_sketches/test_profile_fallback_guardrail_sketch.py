"""Teaching sketch only.

This file is intentionally not part of the default test suite.
It exists to show what a *minimal guardrail test* could look like in Module 2.
"""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app, raise_server_exceptions=False)


def test_profile_invited_user_keeps_safe_fallback_shape() -> None:
    response = client.get("/profile/4")
    assert response.status_code == 200

    data = response.json()
    assert data["name"] == "Diana"
    assert "email" in data
    assert data["email"] is None
