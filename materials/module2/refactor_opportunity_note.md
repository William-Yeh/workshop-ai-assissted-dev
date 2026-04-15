# Module 2｜Refactor Opportunity Note

## 目的
這份說明用來補 Module 2 裡較弱的一條知識點：
- AI 協助辨識 refactor 機會

注意：
本模組不做完整 refactor。  
本模組只要求學員學會：**哪些地方值得先標記為 refactor opportunity。**

---

## 什麼叫 refactor opportunity？
不是「這段 code 我不喜歡」。  
而是：

- 現在雖然可先止血
- 但已經看見重複邏輯 / 邊界模糊 / 規則分裂
- 若不整理，後面還會再出現同類摩擦或事故

---

## 在這個案例裡可以觀察的 refactor signals

### 1. Policy logic 重複
- profile / checkout 對 email 的規則容易散落在不同地方
- 同一條業務規則若在多個 consumer 各自手寫，很容易漂移

### 2. Consumer-specific contract 被混掉
- invited user 與 active verified user 的要求不同
- 若用 generic fallback 蓋掉差異，代表邊界已經不清楚

### 3. Helper / service / adapter 分工不穩
- 原本應該放在 policy / adapter 的判斷，被 patch 臨時塞進別的層
- 這往往是事故後急修留下的痕跡

### 4. Test coverage 的空缺反覆落在同一類情境
- 若 guardrail gap 一直集中在某類 contract / fallback 問題
- 代表不只是「少一個 test」，而可能是 shared design 未整理

---

## 本模組的停損線
只要求學員做到：
- 看出哪些地方值得標記成後續 refactor opportunity
- 寫下一句短 note，說明為什麼

不要求：
- 現在就做完整 refactor
- 現在就改 shared abstraction
- 現在就整理完整 architecture

---

## 可帶走的簡短寫法
- `Refactor opportunity: normalize consumer-specific email policy in one clearer boundary.`
- `Refactor opportunity: avoid duplicating fallback logic across profile and checkout consumers.`
- `Refactor opportunity: separate adapter-level contract normalization from checkout decision logic.`
