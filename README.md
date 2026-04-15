# AI 協作開發｜Module 1 + Module 2 + Module 3 統一教學 Repo

這個 repo 是本課程的**正式定版結構**：

- Module 1、Module 2、Module 3 放在**同一個 git repo**
- 共用同一個 app、同一個 domain、同一套執行環境
- 不拆成兩套重複 app
- 用不同 task pack、materials、tests、git 節點來區分模組

## Start Here
- `MODULES.md`
- `modules/module1/README.md`
- `modules/module2/README.md`
- `modules/module3/README.md`

## 共用執行方式
- 啟動 app：`uv run uvicorn app.main:app --reload`
- 跑測試：`uv run pytest`

## Demo Pages
- `/demo/module1`
- `/demo/profile-ui`
- `/demo/module2`
- `/demo/module3`
