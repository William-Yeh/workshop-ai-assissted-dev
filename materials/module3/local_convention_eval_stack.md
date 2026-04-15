# Module 3｜Local Convention Eval Stack

## 為什麼需要不只一種 eval
local convention 不是寫出一份漂亮 markdown 就算完成。
真正要驗的是：
- 這條 convention 是否真的是從 repo / 文件集抽出來的
- 換一個新任務後，是否真的讓輸出更貼近
- reviewer 是否能靠它看出偏移
- 哪些部分能進一步往 checklist / lint / test / CI 靠

## 四層 eval

### 1. Extraction eval
檢查這條 convention 是否有足夠 evidence，而不是空泛口號。

至少要有：
- 兩個以上 evidence
- scope
- boundary
- counterexample
- why it matters

### 2. Application eval
拿一個 unseen task 做最小對照：
- A：只有 task brief
- B：task brief + local convention card

比較輸出是否更貼近既有 codebase / 文件集。

### 3. Violation-detection eval
準備一份帶有 subtle drift 的輸出，檢查 reviewer 是否能靠這條 convention 指出真正有價值的偏差。

### 4. Enforcement eval
判斷這條 convention 目前最適合落在哪一層：
- reviewer 問句
- checklist
- template 欄位
- lint / test / CI

## 課堂最低要求
課堂中至少做到：
- 1 張 SCOPE card
- 1 次 TRACE eval

若時間足夠，再補：
- 1 次 violation-detection 檢查
- 1 次 AI-assisted 補強與反查
