# neighbor_context.md

## 這個 repo 目前的 local convention

### 命名
- function 名稱採 `snake_case`
- dataclass 欄位名稱也採 `snake_case`
- reason string 會保留 consumer-specific 語意，不用過度抽象的 generic message

### 結構
- `profiles/email_policy.py` 放 policy 判斷
- `checkout/eligibility.py` 放 checkout consumer 的適用邏輯
- `app/main.py` 保持薄，避免把 business logic 塞進 route handler

### 行為
- checkout consumer 有自己的 strict contract
- 不主動把 missing / null / empty string 全部抹平成同一件事
- invited user 與 active verified user 不應被混成同一種規則

### 測試
- tests 目前先固定關鍵 consumer 行為
- 不追求完整 coverage
- 先保住最關鍵的 contract 與 fallback
