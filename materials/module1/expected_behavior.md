# Expected Behavior (Module 1)

This file is a lighter alternative to opening tests first.

## Profile UI expectations

- The profile endpoint should return a displayable `name`.
- The profile UI may safely render a fallback state when email is unavailable for some user states.
- A backend 500 is always worse than a safe fallback state in the profile UI.

## Important distinction

The profile UI contract is **not identical** to the checkout contract.

Examples:

- An invited user may still render safely in the profile UI even when email is unavailable.
- An active verified user without email may still produce a profile response, but that same state can be invalid for downstream checkout decisions.

## Teaching point

Do not assume:

- every missing email is illegal
- every successful response is actually safe
- fixing the profile endpoint alone fixes the broader problem
