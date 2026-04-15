# Module 2 Anti-pattern Demo Pack

## 目的
用反例 demo `2.3.3 風格一致性`，避免只講抽象道德勸說。

## Demo 原則
反例不要做成明顯錯誤；要做成：
- 功能大致可跑
- 測試可能也大多會過
- 但放進現有 codebase 會很突兀

## 建議題型
1. 同功能兩份 patch：選哪份 merge
2. patch 單看沒問題，但和鄰近檔放一起就很怪
3. 測試會過，但 reviewer 不會直接 approve
4. AI patch 讓第二個需求變得更難接

## 觀察面向
- 命名一致性
- 結構一致性
- 行為一致性（error handling / fallback / response shape）
- 測試與交付一致性

## 與 Module 2 的關係
這些 demo 不是要把課講成 style guide 課，
而是要讓學員看到：
**功能能跑，不代表團隊能接手。**


## 本輪已補進 repo 的實體材料
- `style_consistency_demo/bad_patch_example.diff`
- `style_consistency_demo/better_patch_example.diff`
- `style_consistency_demo/neighbor_context.md`
- `style_consistency_demo/review_walkthrough.md`
