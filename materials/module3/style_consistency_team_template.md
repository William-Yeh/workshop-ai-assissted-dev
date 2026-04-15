# Team Shared Template｜Style Consistency Review

## 這份模板用來做什麼？
把「AI 產出是否符合本 repo 既有慣例」整理成團隊共用 reviewer 口徑。

## 何時用
- AI 已交出 patch / test / summary
- 功能看起來可跑，但你懷疑它讓 codebase 更不一致
- 需要讓 reviewer 與作者使用同一套檢查語言

## 檢查面向
### A. 命名一致性
- 命名是否貼近現有 repo？
- 有沒有突然發明第二套名詞？

### B. 結構一致性
- 邏輯放置層次是否合理？
- 有沒有突然引入不必要 abstraction？

### C. 行為一致性
- fallback / error handling / contract 是否延續既有做法？
- consumer-specific expectation 是否被混掉？

### D. 交付一致性
- test style 是否貼近現有測試寫法？
- summary / review note 是否是團隊能接手的格式？

## reviewer 輸出格式建議
1. 哪裡一致
2. 哪裡偏移
3. 偏移風險是什麼
4. 建議先修哪一點

## 邊界提醒
- 這不是審美評論
- 這不是叫 reviewer 重寫全部 patch
- 這是在保護 codebase 不被局部成功、整體失衡的 AI patch 慢慢帶偏
