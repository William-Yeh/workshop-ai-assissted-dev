from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True, frozen=True)
class ProfilePayload:
    name: str
    email: str | None


# Product context:
# profile data is currently sourced from more than one upstream shape.
# this adapter is for the profile UI, which is allowed to render a safe
# fallback state when email is unavailable for some user states.
USERS: dict[int, dict[str, Any]] = {
    1: {
        "name": "Alice",
        "email": "alice@example.com",
        "status": "active",
        "verified": True,
        "account_kind": "member",
    },
    2: {
        "name": "Bob",
        "contact": {"email": "bob@example.com"},
        "lifecycle": {
            "status": "active",
            "verified": True,
            "account_kind": "member",
        },
    },
    3: {
        "name": "Carol",
        "contact": {},
        "lifecycle": {
            "status": "active",
            "verified": True,
            "account_kind": "member",
        },
    },
    4: {
        "name": "Diana",
        "contact": {"email": None},
        "lifecycle": {
            "status": "invited",
            "verified": False,
            "account_kind": "invited",
        },
    },
    5: {
        "name": "Eve",
        "contact": {"email": None},
        "lifecycle": {
            "status": "active",
            "verified": True,
            "account_kind": "member",
        },
    },
}


def get_user_record(user_id: int) -> dict[str, Any]:
    return USERS[user_id]


def build_profile_payload(user: dict[str, Any]) -> ProfilePayload:
    # Current adapter logic is intentionally small for workshop use.
    if "email" in user:
        email = user["email"]
    else:
        email = user["contact"]["email"]

    return ProfilePayload(
        name=user["name"],
        email=email,
    )
