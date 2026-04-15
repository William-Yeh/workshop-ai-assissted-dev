# review_walkthrough.md

## 這個 demo 怎麼用

### Step 1
先只給學員看 `bad_patch_example.diff`，不要先講答案。

請他們回答：
1. 這份 patch 會不會讓 codebase 更不一致？
2. 哪些地方雖然功能可能可跑，但和既有 repo 寫法不合？
3. 哪些地方把 consumer-specific 規則偷偷抹平了？

### Step 2
再給 `neighbor_context.md`，讓學員對照現有 repo 慣例。

### Step 3
再給 `better_patch_example.diff`，讓學員比較：
- 哪個版本比較延續既有 pattern
- 哪個版本比較適合 first-layer review 後收斂進 repo

## 講師回收重點
- 壞 patch 的問題，不是只有功能對不對
- 更重要的是：
  - invent 了第二套命名
  - 重複 policy logic
  - 混掉 consumer-specific contract
  - 把 strictness 用 generic fallback 蓋掉

## 結尾句
這不是審美問題。  
這是在判斷：這份 AI patch 是不是只在局部能跑，卻讓整個 codebase 更不一致。
