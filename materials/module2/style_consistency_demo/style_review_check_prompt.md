# Style Review Self-check Prompt

請不要再幫我優化功能。

請改用 reviewer 角度檢查這份修改，回答：
1. 哪些地方不符合現有專案風格 / 慣例 / 結構選擇？
2. 哪些地方雖然能跑，但會讓 codebase 更不一致？
3. 哪些地方像是 invent 了第二套寫法？
4. 如果只能保留既有 pattern，這份 patch 應怎麼收斂？
5. 請把問題分成：
   - 風格一致性
   - 結構一致性
   - 品質風險
