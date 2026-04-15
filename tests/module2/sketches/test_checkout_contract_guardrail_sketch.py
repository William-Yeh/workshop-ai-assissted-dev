from __future__ import annotations

"""Module 2 sketch only.

Teaching purpose:
- This is not a final test.
- It shows where a guardrail test could help distinguish
  profile UI fallback from checkout eligibility rules.

Students should decide:
- Is this the cheapest validation move right now?
- Or should they first inspect contracts / policy / code flow?
"""


def test_checkout_contract_guardrail_sketch() -> None:
    # sketch:
    # 1. active verified user without real email should not be eligible
    # 2. invited user may proceed in limited state
    # 3. do not collapse these two consumer expectations into one rule
    assert True
