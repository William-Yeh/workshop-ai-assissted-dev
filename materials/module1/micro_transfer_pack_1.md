# Module 1 微型遷移包 1｜同 repo 變體：`/profile/4`

## 用途
這題延續主案例的 profile 脈絡，但把問題型態從 **hard failure** 轉成 **可 render 的 fallback**。

## 現象
- `/profile/4` 回 200
- `email` 為 `null`
- profile UI 可安全 fallback 成「Email missing」

## Naive prompt
> The `/profile` response looks wrong. Please find the issue and fix it.

## 學員任務
請把上面的 prompt 改寫成較穩的 task brief。至少要補出：

1. 現在發生了什麼
2. 你現在要 AI 先做什麼
3. 你希望它怎麼輸出
4. 你最後一句怎麼把 AI 收住

## 講師回收點
- 有沒有把「問題」改寫成「先判斷這是不是違反 profile UI expectation」
- 有沒有避免直接要求 patch
- 有沒有指定可檢查輸出
- 有沒有寫出一個有用的 final line

## 教學提醒
這題的關鍵不是修 code，而是看見：
- 200 不等於沒問題
- 缺 email 不等於一定非法
- prompt 要跟 consumer contract 一起寫
