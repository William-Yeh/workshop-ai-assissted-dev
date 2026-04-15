from __future__ import annotations

"""Teaching note: This file makes the current contract assumptions visible for Module 1.

It is intentionally small. Its job is not to implement validation logic in full.
Its job is to make these distinctions explicit:

- email field missing
- email field present but null
- email field present but empty string
- which consumer is reading the value
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProfileUiContract:
    name_required: bool = True
    email_nullable_for_some_user_states: bool = True
    safe_missing_email_label: str = "Email missing"


@dataclass(frozen=True, slots=True)
class CheckoutContract:
    active_verified_user_requires_real_email: bool = True
    invited_user_may_complete_email_later: bool = True


PROFILE_UI_CONTRACT = ProfileUiContract()
CHECKOUT_CONTRACT = CheckoutContract()

NULLABLE_AND_MISSING_SEMANTICS = {
    "missing_field": "The field is absent from the payload entirely.",
    "null_value": "The field exists but is explicitly null.",
    "empty_string": "The field exists but has been coerced to an empty string.",
    "teaching_point": (
        "These states may look similar in the UI, "
        "but they should not always be treated as identical during analysis."
    ),
}
