from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app, raise_server_exceptions=False)


def test_profile_old_shape_still_works() -> None:
    response = client.get("/profile/1")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Alice",
        "email": "alice@example.com",
    }


def test_profile_new_shape_happy_path_works() -> None:
    response = client.get("/profile/2")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Bob",
        "email": "bob@example.com",
    }


def test_profile_missing_nested_email_still_breaks_with_server_error() -> None:
    response = client.get("/profile/3")
    assert response.status_code == 500


def test_profile_ui_can_render_missing_email_for_invited_user() -> None:
    response = client.get("/profile/4")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Diana",
        "email": None,
    }


def test_checkout_rejects_active_verified_user_without_email() -> None:
    response = client.get("/checkout-eligibility/5")
    assert response.status_code == 200
    assert response.json() == {
        "user_id": 5,
        "eligible": False,
        "reason": "missing email for active verified user",
    }


def test_checkout_allows_invited_user_to_complete_email_later() -> None:
    response = client.get("/checkout-eligibility/4")
    assert response.status_code == 200
    assert response.json() == {
        "user_id": 4,
        "eligible": True,
        "reason": "email can be completed later for invited or phone-only users",
    }


def test_demo_page_shows_checkout_panel() -> None:
    response = client.get("/demo/profile-ui")
    assert response.status_code == 200
    text = response.text
    assert "Checkout Eligibility" in text
    assert "profile UI fallback and checkout eligibility are not the same contract" in text
