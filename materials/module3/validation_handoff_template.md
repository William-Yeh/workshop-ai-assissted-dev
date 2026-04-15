# Team Shared Template｜Validation / Diagnosis Handoff

## 這份模板用來做什麼？
把分析任務整理成團隊可接手的格式，避免每次都把 symptom、猜測、驗證順序混在一起。

## 使用時機
- bug / incident / review 任務還不適合直接 patch
- 需要先縮小問題範圍
- 需要讓下一位接手者知道目前分析到哪裡

## 固定欄位
### 1. Symptom
- 目前看見的是什麼現象？
- 哪些是事實？

### 2. Candidate causes
- 目前有哪些候選原因？
- 哪些只是推測？

### 3. Still-missing information
- 還缺哪些關鍵資訊？
- 缺了它，哪些判斷不該先做？

### 4. Validation order
- 下一步先驗哪一條？
- 為什麼這一步成本較低、資訊價值較高？

### 5. First-layer quality delivery
- 目前先交哪一種品質產物？
- analysis note / focused review / minimal test sketch / PR summary？

## local convention 提醒
分析任務也有 local convention，例如：
- incident summary 的順序
- hypothesis 的寫法
- evidence 包的命名或結構
- 先驗哪一層的團隊慣例

先把這些寫進 SCOPE card，再整理進 handoff。

## 最低驗證
- symptom 與 cause 沒有混在一起
- validation order 有先後理由
- local convention 有被保留
- 沒有太早跳進完整修復
