from __future__ import annotations

from typing import Any


def lifecycle_status(user: dict[str, Any]) -> str:
    if "status" in user:
        return str(user["status"])
    return str(user.get("lifecycle", {}).get("status", "unknown"))


def account_kind(user: dict[str, Any]) -> str:
    if "account_kind" in user:
        return str(user["account_kind"])
    return str(user.get("lifecycle", {}).get("account_kind", "unknown"))


def is_verified(user: dict[str, Any]) -> bool:
    if "verified" in user:
        return bool(user["verified"])
    return bool(user.get("lifecycle", {}).get("verified", False))


def is_email_missing_allowed(user: dict[str, Any]) -> bool:
    """A missing email is allowed for invited and phone-only onboarding users.

    It is not allowed for active verified users.
    """
    kind = account_kind(user)
    status = lifecycle_status(user)
    verified = is_verified(user)

    if kind in {"invited", "phone_only"}:
        return True
    if status == "active" and verified:
        return False
    return True


def is_email_required_for_checkout(user: dict[str, Any]) -> bool:
    """Checkout is stricter than the profile UI.

    Active verified users must have a real email.
    Invited users may proceed in a limited state and complete email later.
    """
    status = lifecycle_status(user)
    verified = is_verified(user)
    return status == "active" and verified
