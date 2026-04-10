# Module 1 微型遷移包 2｜第二個小型案例：`/checkout-eligibility/5`

## 用途
這題把學員從 profile UI 帶到 **更嚴格的 downstream consumer**。重點不是做 checkout flow，而是讓學員看見：同樣是 missing email，不同 consumer 的問題定義不同。

## 現象
- `/profile/5` 回 200
- profile UI 仍可 render fallback
- `/checkout-eligibility/5` 回 200
- 但 `eligible` 為 `false`
- `reason` 為 `missing email for active verified user`

## Naive prompt
> The user cannot checkout because email is missing. Please fix it.

## 學員任務
請把上面的 prompt 改寫成較穩的 task brief。至少要補出：

1. 現在發生了什麼
2. 你現在要 AI 先做什麼
3. 你希望它怎麼輸出
4. 你最後一句怎麼把 AI 收住

## 講師回收點
- 有沒有交代這是 checkout consumer，而不是單純 profile 問題
- 有沒有避免直接把 profile UI fallback 當成 checkout contract
- 有沒有把 request 收成「先釐清 consumer requirement」而不是直接 patch
- 有沒有用輸出格式幫助判斷「哪一層在出問題」

## 教學提醒
這題的難度增加在 **prompt 判斷**，不是技術深度。
