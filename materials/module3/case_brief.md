# Module 3 Case Brief

## 模組定位
Module 3 的重點不是再教一次 prompt 技巧。
它要處理的是：
- 從 Module 1 與 Module 2 已驗證有效的做法中，抽出可遷移的協作結構
- 把 repo / 文件集內真正有用的 local convention 顯性化
- 用 evals 檢查這些 convention 是否真的能改善新任務輸出
- 在最後示範：這整個提取、驗證過程也可以跟 AI 協作

## 本模組真正要解的問題
常見問題不是「大家都不會下 prompt」，而是：
- 個人有招，但別人接不起來
- 有 prompt，但沒有使用條件、輸入需求、驗證點與停損線
- 有 style consistency 提醒，但沒有真的抽出 repo / 文件集的 local convention
- 有 convention markdown，但套到新任務時不見得真的有用

## 本模組核心任務
把個人有效做法整理成最少包含以下兩層的共用資產：
1. **共通骨架**：哪些欄位與判準，換一個相近任務仍成立
2. **在地慣例**：哪些做法屬於這個 repo / 文件集的 local convention，必須保留

## 本模組的三個主產物
1. `local convention inventory`
2. `local convention card`（用 SCOPE 留欄位）
3. `TRACE eval`（檢查這條 convention 是否真的有效）

## SCOPE card 最少欄位
- **S — Signal**：你看到了什麼 repeated pattern
- **C — Context**：這條 convention 適用在哪裡
- **O — Out-of-scope**：哪些情況不要硬套
- **P — Proof**：至少 2 個 repo / 文件集中的 evidence
- **E — Enforcement path**：它目前停在 reviewer / checklist / template，還是可往 lint / test / CI 推進

## TRACE eval 最少判準
- **T — Transferable**：換個相近任務還能用嗎
- **R — Repeat-backed**：有沒有足夠 evidence 支撐
- **A — Actionable**：是否可操作、可檢查
- **C — Context-bounded**：scope / boundary 是否清楚
- **E — Effective**：加上它後，輸出是否真的更貼近 codebase / 文件集

## 建議承接來源
優先從以下資產挑一個來做 local convention extraction：
- Module 1 的 task brief 外層骨架
- Module 2 的 validation order 寫法
- Module 2 的 style consistency 自查口徑
- Module 2 的 first-layer quality delivery 寫法

## 本模組可交付物
1 小時版建議以下三選一，不要全部做：
- 1 張 local convention card
- 1 份 shared task brief 模板草稿
- 1 份 validation / diagnosis handoff 模板草稿

但無論選哪一個，都要補：
- 1 次 TRACE eval 草稿
- 1 段 AI-assisted 驗證觀察

## 停損線
本模組停在：
- 可遷移結構
- local convention
- evals
- checklist / template / reviewer language
- human-first、AI-assisted 示範

本模組不要求：
- workflow gate
- team-level enforcement rule
- automated review rule
- CI / bot / policy integration

以上內容留到 Module 4。
