# Module 3｜Start Here

## 角色
Module 3 承接 Module 1 與 Module 2。
它現在不只是整理 template pack，而是正式在教三件事：
1. 從既有做法抽出可遷移的協作結構
2. 辨認、提取、保存 local convention
3. 用 evals 檢查這些 convention 是否真的能改變輸出

本模組仍然**不直接進 workflow 治理**。
workflow gate、team-wide rule、CI policy、automation 留到 Module 4。

## 先看
1. `materials/module3/module3_task_pack.md`
2. `materials/module3/case_brief.md`
3. `materials/module3/local_convention_inventory_template.md`
4. `materials/module3/local_convention_card_template.md`
5. `materials/module3/local_convention_trace_eval.md`
6. `materials/module3/local_convention_eval_stack.md`
7. `materials/module3/ai_assisted_convention_extraction_demo.md`
8. `materials/module3/template_pack_checklist.md`
9. `materials/module3/shared_task_brief_template.md`
10. `materials/module3/validation_handoff_template.md`
11. `materials/module3/style_consistency_team_template.md`
12. `materials/module3/ai_outsource_judgment_table.md`

## repo 內主要入口
- UI：`/demo/module3`
- 對照頁面：`/demo/module1`、`/demo/module2`
- 測試：
  - `tests/module3/test_module3_demo_index.py`
  - `tests/module3/test_module3_materials.py`

## 教學焦點
- 從具體案例抽出可遷移原則
- 用 SCOPE card 留住 local convention
- 用 TRACE 檢查 local convention 是否真的有效
- human-first、AI-assisted 的提取與驗證流程
- 不要太早跳進 team-level workflow / rules

## 建議授課節奏
### 壓在 60 分鐘內
建議只要求學員完成：
- 1 份 inventory
- 1 張 SCOPE card
- 1 次 TRACE eval 草稿

### 放寬到 60～70 分鐘
建議再加：
- 1 段 human-first / AI-assisted 示範
- 1 個 reviewer / violation-detection 檢查

## 停損線
三種 template pack 全做完，通常會超時。
本模組較穩的設計，是：
- **1 個主 deliverable：local convention card**
- **1 個 eval：TRACE**
- **1 個短示範：AI-assisted 補強與反查**
