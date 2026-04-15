# Better Patch Review Points｜對照看什麼

對照 `commerce_platform/profiles/service.py` 與既有測試時，請至少檢查：

1. 有沒有延續既有 `ProfilePayload` 結構
2. 有沒有 invent 新 helper / abstraction / dependency
3. 命名是否延續現有 repo 習慣
4. fallback 行為是否和既有 contract / consumer expectation 一致
5. 測試若要補，是否只補最小、局部、夠用的 guardrail
