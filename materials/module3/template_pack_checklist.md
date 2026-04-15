# Module 3｜Template Pack Checklist

## 先過 local convention，再談 template
這份 checklist 的目的，不是把模板寫得很漂亮。
它是用來防止：
- 模板只對原作者有用
- 模板只有 prompt、沒有 local convention
- 模板只有規則口號、沒有 evidence
- 模板讓 AI 太早跨過人類該守的邊界

## A. 候選 convention 是否站得住
### 1. 有 Signal，不是印象流
- 這條做法是不是在 repo / 文件集中重複出現？

### 2. 有 Proof，不是冠冕堂皇
- 至少有 2 個 evidence 嗎？

### 3. 有邊界，不是萬用句
- 何時適用？
- 何時不要硬套？

### 4. 有成本，不是審美偏好
- 違反後會增加什麼成本？

## B. TRACE 是否過關
### T — Transferable
- 換一個相近任務，這條 convention 還成立嗎？

### R — Repeat-backed
- evidence 是否足夠支撐？

### A — Actionable
- reviewer 能根據它指出哪裡不對嗎？

### C — Context-bounded
- scope / out-of-scope 是否清楚？

### E — Effective
- 加上它後，輸出是否真的更貼近 codebase / 文件集？

## C. 若要整理成 template，至少還要有什麼
### 1. 用途清楚
- 這份模板是拿來解哪一類問題？

### 2. 使用時機清楚
- 何時用？何時不要用？

### 3. 輸入條件清楚
- 需要哪些檔案、log、案例、鄰近 code、需求說明？

### 4. 最小足夠 context 清楚
- 是否有把關鍵 consumer、邊界、局部慣例講清楚？

### 5. 輸出格式清楚
- 希望 AI 交出什麼？分析草稿、review note、patch sketch、還是 handoff？

### 6. 驗證點與交接點清楚
- 人類最後至少要驗什麼？
- 下一位接手者應先看什麼？

### 7. AI 邊界清楚
- 哪些事情 AI 可以先做？
- 哪些事情 AI 只能先做草稿？
- 哪些事情不應直接外包？
