# Challenge Pack — Profile Identity Data Migration Incident

You are looking at a small product codebase for a membership and orders platform.

## What you are told

The team reports that the **profile feature is broken**. What they mean by "broken" is not fully clear yet.

You should not assume:

- there is only one bug
- the problem is only in the backend
- every missing email is illegal
- the first patch you can make is the right patch to merge

## Your task

Before proposing a fix, first figure out:

1. What symptoms actually exist
2. Whether they belong to the same problem or different problem layers
3. What information is still missing
4. Which consumer contracts matter here
5. What should be verified first
6. What would count as an acceptable fix

## Suggested starting points

- run the app
- inspect `/demo/profile-ui`
- inspect `/profile/{user_id}`
- inspect `/checkout-eligibility/{user_id}`
- run the tests
- inspect the profile-related code path

## Important

Do **not** jump directly to a patch.

Start by producing:

- known facts
- missing information
- likely causes
- consumer-specific requirements
- verification order
- fix options with trade-offs
