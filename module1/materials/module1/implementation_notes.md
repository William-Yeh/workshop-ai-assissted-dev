# Module 1 Artifact Implementation Notes

## 本次實作內容
這份 artifact 不是完整 workshop repo，而是 Module 1 可直接 demo、可延伸 refine 的基底。

### 已完成
- 保留原本 `module1` 的最小可執行結構
- 擴充 `/demo/profile-ui`
- 新增 **Checkout Eligibility** 視覺區塊
- 用同一個頁面同時展示：
  - Profile API 結果
  - Profile UI 可否安全 render
  - Checkout eligibility 結果
- 補上兩份微型遷移包：
  - `micro_transfer_pack_1.md`
  - `micro_transfer_pack_2.md`

## 這次設計的原則
- 不做完整 checkout flow
- 不把 Module 1 做成第二個產品 demo
- 只做「決策可視化 UI」
- 讓學員看見：
  - hard failure
  - safe fallback
  - stricter downstream consumer

## 建議教學順序
1. `/profile/3`：hard failure
2. `/profile/4`：safe fallback
3. `/checkout-eligibility/5`：stricter consumer

## 後續 refine 建議
- Module 2 再正式引入 BRIEF / RAISE
- Module 1 維持 task brief 外層骨架，不公開框架名
- 若要擴充 UI，也應優先增加「對比感」，而不是增加功能量
