# Module 2｜Task Pack v1

## 使用方式
本任務包的目的，是讓學員在 VSCode / Cline 裡真的做一輪：

- 問題分析
- 驗證排序
- 最小測試判斷
- 第一層品質交付

這不是完整 debug 工作坊。  
也不是品質工程大全。  
請守住停損線：**縮小範圍、排驗證順序、補第一層品質交付。**

---

## 先讀
1. `materials/module2/case_brief.md`
2. `materials/module2/symptom_matrix.md`
3. `materials/module2/evidence_pack.md`
4. `materials/module2/test_gap_note.md`

---

## 任務 A｜整理問題分析草稿
### 目標
把 symptom、candidate causes、still-missing information 分開。

### 建議操作
- 打開 `materials/module2/validation_order_template.md`
- 先不要修 code
- 先根據 evidence pack 填出：
  - symptom
  - candidate causes
  - still-missing information

### 預期產出
- 一份問題分析草稿

---

## 任務 B｜排驗證順序
### 目標
決定「現在先驗哪一條」。

### 建議操作
- 參考 `materials/module2/validation_order_template.md`
- 評估哪個 validation move 最便宜、最能排除候選原因：
  - log / stack trace
  - contract 對照
  - code flow / dependency 對照
  - focused review
  - 最小 failing test
  - guardrail test

### 預期產出
- 一份 validation order 草稿
- 一句話說明：為什麼現在先驗這一條

---

## 任務 C｜判斷是否值得先補最小 test
### 目標
判斷 test 在這裡是不是一個合理的 validation move。

### 建議操作
- 看 `materials/module2/test_gap_note.md`
- 看 `tests/module2/sketches/`
- 用這三個判準判斷：
  1. 這個 test 能不能區分候選原因？
  2. 這個 test 能不能固定關鍵預期行為？
  3. 這個 test 是不是最小、局部、夠用？

### 預期產出
- 一份 test decision note
- 或一個最小 test sketch 的補充說明

---

## 任務 D｜做第一層 quality delivery
### 目標
不要把問題做完，只要先交出團隊能接手的第一層品質版本。

### 可選產出（擇一）
1. focused review notes
2. 最小 test sketch
3. style consistency review
4. PR / issue summary

### 可參考材料
- `materials/module2/first_layer_quality_checklist.md`
- `materials/module2/style_consistency_checklist.md`
- `materials/module2/style_consistency_demo/`
- `materials/module2/micro_transfer_2_review_test_pack/`

---

## 任務 E｜做 style consistency review
### 目標
判斷一份 AI patch 是否只是局部能跑，但會讓 codebase 更不一致。

### 建議操作
- 先看 `materials/module2/style_consistency_demo/bad_patch_example.diff`
- 不要先看答案，先自己 review
- 再看：
  - `neighbor_context.md`
  - `better_patch_example.diff`
  - `review_walkthrough.md`

### 預期產出
- 一份 style drift spotting note
- 或一份 reviewer self-check 結果

---

## 交付格式建議
你最後至少交出以下其中一項：
- 問題分析草稿
- validation order 草稿
- test decision note
- style consistency review
- PR / issue summary

---

## 講師停損線
- 不要求完整 patch
- 不要求完整測試策略
- 不要求完整 refactor
- 不要求完整品質工程治理

---

## 結尾提醒
你現在不是要「把問題做完」。  
你現在是在練：

- 先把問題講清楚
- 先把驗證排對
- 先把第一層品質交付做出來
