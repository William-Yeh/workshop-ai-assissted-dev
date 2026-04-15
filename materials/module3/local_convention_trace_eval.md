# Module 3｜TRACE Eval Sheet

## T — Transferable
- 換一個相近任務，這條 convention 還成立嗎？
- 去掉原案例專有名詞後，還有意義嗎？
- 是否適合用一個 unseen task 做最小驗證？

## R — Repeat-backed
- evidence 是否足夠？
- 是兩個以上獨立例子，還是只是一個案例的不同表面？
- 這條 convention 來自 codebase / 文件集的重複，還是只是單一作者偏好？

## A — Actionable
- reviewer 能根據這條 convention 指出哪裡偏了嗎？
- 新人看得懂怎麼套用嗎？
- 這條 convention 能否轉成 checklist / reviewer 問句？

## C — Context-bounded
- 適用範圍清楚嗎？
- 哪些情況不要硬套？
- 是否已寫出至少一個 counterexample？

## E — Effective
請至少做一個最小對照：
- A：只有 task brief
- B：task brief + local convention card

比較：
- 命名是否更貼近 repo？
- 結構是否更貼近既有做法？
- 術語 / summary / handoff 是否更一致？
- reviewer comment 是否減少明顯偏移？

## Reviewer / violation-detection 檢查
除了 A/B 對照，也請補問：
- 能否用這條 convention 看出一個 subtle violation？
- 若看到一份表面上格式正確、但其實不貼近 codebase / 文件集的輸出，這條 convention 能指出哪裡不對嗎？

## 評語
這條 convention 目前應該：
- 保留為 reviewer language
- 升格成 checklist / template
- 暫時不要固定
- 可往 lint / test / CI 推進
