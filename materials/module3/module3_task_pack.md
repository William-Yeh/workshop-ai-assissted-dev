# Module 3｜Task Pack v3

## 使用方式
本任務包的目的，是讓學員把「自己會用的 AI 協作做法」，整理成別人也能接手、也能驗證的團隊資產。

這不只是模板課。
它同時是：
- 抽出可遷移原則
- 保留 local convention
- 用 evals 檢查這份 convention 是否真的有效
- 最後示範如何跟 AI 協作完成這件事

## 先讀
1. `materials/module3/case_brief.md`
2. `materials/module3/local_convention_inventory_template.md`
3. `materials/module3/local_convention_card_template.md`
4. `materials/module3/local_convention_trace_eval.md`
5. `materials/module3/local_convention_eval_stack.md`
6. `materials/module3/ai_assisted_convention_extraction_demo.md`
7. `materials/module3/template_pack_checklist.md`

## 任務 A｜觀察 repeated patterns
### 目標
先不要急著寫 prompt。先找 repo / 文件集裡反覆出現的 pattern。

### 建議來源
- 鄰近 code
- 鄰近測試
- summary / review note / handoff note
- 既有命名、結構、術語、驗證順序

### 預期產出
- 一份 local convention inventory 草稿

## 任務 B｜寫出 1 張 SCOPE card
### 目標
把一條 candidate local convention 寫成可以交接、可檢查的格式。

### 最少欄位
- Signal
- Context
- Out-of-scope
- Proof
- Enforcement path

### 預期產出
- 一張 local convention card

## 任務 C｜做 1 次 TRACE eval
### 目標
不是只看文件寫得漂亮，而是要檢查這條 convention 是否真的有效。

### 最少要回答
1. 換一個相近任務還能用嗎？
2. evidence 是否足夠？
3. reviewer 能看出違反嗎？
4. 加上這條 convention 後，輸出有沒有更貼近 repo / 文件集？

### 預期產出
- 一份 TRACE eval 草稿

## 任務 D｜human-first，AI-assisted
### 目標
先用人類方法做一輪，再請 AI 協助補 evidence、產生反例、模擬 reviewer、設計 unseen task。

### 預期產出
- 一段 AI-assisted 補強記錄
- 一句話說明：AI 幫了什麼，人最後仍要決定什麼

## Stretch goal｜再把它整理成 template pack
若時間足夠，再從 local convention card 往下整理成：
- shared task brief template
- validation / diagnosis handoff template
- style consistency review template

## 建議時數
- **核心版：55～60 分鐘**
  - inventory
  - 1 張 SCOPE card
  - 1 次 TRACE eval
- **完整但仍可控：60～70 分鐘**
  - 核心版全部
  - 再加 1 段 AI-assisted 示範
  - 再加 1 次 reviewer / violation-detection 檢查

## 停損線
若時間開始往 70 分鐘靠近，請優先保留：
- 1 份 inventory
- 1 張 SCOPE card
- 1 次 TRACE eval

不要同時要求三種 template pack 全做完。
