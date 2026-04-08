# Release Note Excerpt

## Recent change
The identity profile feature is in the middle of an upstream data-shape transition.

This transition was expected to be backward compatible during rollout.

## Known risk areas during rollout
- field location differences between upstream sources
- missing optional fields
- nullable values that are valid for some user states
- mismatch between API response assumptions and UI display assumptions
- downstream consumers with stricter requirements than the profile UI

## Product note
The profile UI is allowed to render a safe fallback state for some users.
Checkout-related decisions are stricter and should not silently coerce missing email into a "good enough" value.
