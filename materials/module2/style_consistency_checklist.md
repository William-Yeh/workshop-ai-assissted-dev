# Module 2｜Style Consistency Checklist

## 這一頁要回答什麼？
- 這份 AI 產出是不是符合專案既有風格 / 慣例 / 結構選擇？
- 這份修改是不是會讓 codebase 更不一致？
- 這份 patch 是不是只在功能上能跑，但風格上很突兀？

## 看四個面向

### A. 命名一致性
- function / variable / response field 命名是否貼近現有 repo？
- 有沒有突然 invent 第二套命名宇宙？

### B. 結構一致性
- logic 放的層次是否貼近既有做法？
- 有沒有把原本應放在 service 的邏輯塞進 controller？
- 有沒有突然加一層新的 abstraction？

### C. 行為一致性
- error handling / fallback 是否延續既有慣例？
- response shape / contract 是否和相鄰功能一致？
- consumer expectation 是否被混成同一套規則？

### D. 測試與交付一致性
- test style 是否貼近既有測試寫法？
- PR / issue summary 是否是團隊能接手的語氣與結構？

## 講師提醒
這不是在教「審美」。  
這是在教：不要讓 AI patch 只在局部能跑，卻讓整個 codebase 更不一致。
