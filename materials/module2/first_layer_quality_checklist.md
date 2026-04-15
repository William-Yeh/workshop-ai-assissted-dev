# Module 2｜First-layer Quality Checklist

## 目的
這不是完整品質工程清單。  
這是 Module 2 用來做第一層品質交付的輕量 checklist。

## 檢查面向

### 1. 正確性
- 這份分析 / patch / test sketch 是否對準真正的 symptom？
- 是否把 symptom 與 candidate causes 分開？

### 2. 相容性
- 是否符合既有 contract / consumer expectation？
- 是否會破壞既有 response shape 或 fallback 行為？

### 3. 風格一致性
- 是否延續既有命名方式？
- 是否延續既有 error handling / fallback 慣例？
- 是否延續既有 helper / service / controller 分工？
- 是否延續既有 test style？

### 4. 可交付性
- 現在是否已足夠進入下一輪討論？
- 是否已寫出 validation order / review notes / test sketch / PR summary 其中之一？

## 收尾提醒
目標不是把問題做完。  
目標是交出一個團隊能接手的第一層品質版本。
