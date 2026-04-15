# Module 2 Evidence Pack

## Incident framing
目前 repo 裡最值得用來教 Module 2 的，不是「找唯一 bug」，而是：
- 同一個 missing email 現象，為什麼會在不同 consumer 產生不同後果？
- 什麼時候應該先看 contract / policy / code flow？
- 什麼時候值得補一個最小 test？

## Evidence 1: Existing stable behavior
`tests/test_profile_api.py` 已固定幾個 baseline：
- old shape works
- new shape happy path works
- invited user can render fallback
- checkout is stricter for active verified users

## Evidence 2: Hard failure
`/profile/3` 仍然 500。
這個 symptom 容易讓人太快跳到 patch，但教學上應先問：
- 這是單一 adapter bug？
- 還是 contract migration 尚未完成？
- 哪些 evidence 最能先排除一條路？

## Evidence 3: Consumer mismatch
`/profile/4` 與 `/checkout-eligibility/5` 顯示：
- profile UI fallback
- checkout strict validation
不是同一種 contract。

## Evidence 4: Policy layer
`commerce_platform/profiles/email_policy.py` 已明示：
- invited / phone-only onboarding users
- active verified users
對 missing email 的容忍度不同。

## 建議引導問題
1. 現在的 symptom 是什麼？
2. 哪些是 candidate causes？
3. 還缺什麼資訊？
4. 哪個 validation move 最便宜？
5. 哪個 validation move 最能區分候選原因？

## 可用 validation moves
- 看 log / stack trace
- 對照 response / contract
- 看 policy 與 consumer expectation
- focused code review
- 補一個最小 guardrail test
