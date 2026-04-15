# Module 2 Case Brief

## 模組定位
Module 2 的重點不是讓 AI 給更多建議，而是讓它幫忙：
- 縮小問題範圍
- 排驗證順序
- 補第一層品質交付

本案例不要求完整修 bug，也不要求完整測試策略或完整品質工程治理。

## 主案例（工作版暫定）
**Profile migration incident：從症狀到驗證順序**

## 教學目標
學員應能：
1. 分開處理 symptom、candidate causes、still-missing information
2. 提出一個成本較低、可縮小範圍的 validation order
3. 交出第一層品質交付，而不是直接做完整修復

## 已知材料
- `app/main.py`
- `commerce_platform/profiles/service.py`
- `commerce_platform/checkout/eligibility.py`
- `commerce_platform/profiles/email_policy.py`
- `tests/test_profile_api.py`
- `materials/module2/symptom_matrix.md`
- `materials/module2/evidence_pack.md`
- `materials/module2/test_gap_note.md`

## 本模組可交付物
以下擇一或組合完成：
- 問題分析草稿
- 驗證順序草稿
- focused review checklist
- 最小 test sketch
- PR / issue summary

## 停損線
本模組停在：
- diagnosis
- validation order
- first-layer quality delivery

本模組不要求：
- 完整 patch
- 完整 refactor
- 完整測試策略
- 完整治理規則
