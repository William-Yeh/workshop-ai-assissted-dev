from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from commerce_platform.profiles.email_policy import is_email_required_for_checkout


@dataclass(slots=True, frozen=True)
class CheckoutEligibility:
    user_id: int
    eligible: bool
    reason: str


def extract_email_for_checkout(user: dict[str, Any]) -> str | None:
    # This consumer is strict about preserving the difference between
    # missing and null in the adapter layer. It does not coerce to "".
    if "email" in user:
        return user["email"]
    return user.get("contact", {}).get("email")


def evaluate_checkout_eligibility(user_id: int, user: dict[str, Any]) -> CheckoutEligibility:
    email = extract_email_for_checkout(user)
    email_required = is_email_required_for_checkout(user)

    if email_required and not email:
        return CheckoutEligibility(
            user_id=user_id,
            eligible=False,
            reason="missing email for active verified user",
        )
    if not email_required and not email:
        return CheckoutEligibility(
            user_id=user_id,
            eligible=True,
            reason="email can be completed later for invited or phone-only users",
        )
    return CheckoutEligibility(
        user_id=user_id,
        eligible=True,
        reason="eligible",
    )
