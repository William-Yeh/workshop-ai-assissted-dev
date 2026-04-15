# test gap note

## 已有 baseline tests
- `/profile/1` 舊 shape 正常
- `/profile/2` 新 shape 正常
- `/profile/3` 缺 nested email 目前仍回 500
- `/profile/4` invited user 缺 email 但 profile UI 可接受
- `/checkout-eligibility/5` active verified user 缺 email 不可 checkout
- `/checkout-eligibility/4` invited user 可稍後補 email

## 值得先補最小 test 的地方
### Gap A｜profile UI 的 safe fallback contract 還沒有被獨立固定
可以補一個最小 test，確認 `/profile/4` 的 fallback 行為不會被未來修改偷偷改成 `""`、`missing key` 或其他自創 shape。

### Gap B｜active verified user 在 profile UI 與 checkout 的差異仍可再被明確化
可補一個最小 guardrail test，強化學員對「同樣缺 email，但不同 consumer expectation 不同」的理解。

## 不建議一開始先補 test 的地方
- `/profile/3` 的 500 若 symptom / cause 尚未分清，不要一開始就補一整套測試
- 若目前還在釐清是 adapter bug、contract drift、還是 consumer mismatch，先看 log / code flow / contract 對照更便宜
