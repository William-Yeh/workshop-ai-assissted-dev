# Module 2 Symptom Matrix

| symptom | where it appears | reproducibility | possible consumer impact | known / unknown |
|---|---|---|---|---|
| `/profile/3` returns 500 | profile API | stable | profile UI hard failure | known: nested email missing; unknown: should UI fallback apply here? |
| `/profile/4` returns 200 with `email: null` | profile API / profile UI | stable | profile UI can still render fallback | known: invited user may continue without email; unknown: where should this rule live? |
| `/checkout-eligibility/5` rejects active verified user without email | checkout consumer | stable | checkout blocked | known: checkout is stricter than profile UI; unknown: is profile payload hiding a stricter downstream contract? |
| two consumers interpret the same missing email differently | profile UI vs checkout | stable | inconsistency risk / wrong fix direction | known: consumer expectations differ; unknown: should fix happen in adapter, policy, or consumer-specific validation? |

## Teaching note
這張表的目的，不是把答案直接給學員，而是讓學員先把：
- symptom
- consumer
- still-missing information

分開來看。
