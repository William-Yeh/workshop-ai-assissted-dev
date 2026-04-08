from __future__ import annotations


def normalize_email(value: str | None) -> str:
    """
    WARNING:
    This helper is intentionally included for workshop discussion.

    It is convenient, but it also collapses:
    - missing field
    - null
    - empty string

    into the same representation.
    That may make one consumer look fixed while hiding a migration or data-quality problem.
    """
    return value or ""
