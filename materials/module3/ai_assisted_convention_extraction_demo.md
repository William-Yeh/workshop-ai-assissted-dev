# Module 3｜AI-Assisted Convention Extraction Demo

## 示範定位
這一段放在模組後段。
先讓學員用人類方法做一輪，再示範如何請 AI 協助提取、補證據、產生反例、設計 eval。

## 原則
- **human-first**：判準先由人建立
- **AI-assisted**：AI 幫你加速、補強、反查
- **human-decides**：最終採納、邊界、是否升格成規則，仍由人決定

## 可以請 AI 幫的事
1. 從既有檔案找更多 repeated patterns
2. 為候選 convention 補 proof / counterexample
3. 將 inventory 重整成 SCOPE card 草稿
4. 產生一個 unseen task
5. 充當 reviewer，挑戰這條 convention 是否過度泛化
6. 幫你設計最小 A/B 對照
7. 嘗試指出一個 subtle violation

## 不應直接外包給 AI
- 哪條 convention 要正式採納
- 適用範圍與例外的最終判斷
- 是否升格成 team-level rule
- 是否進入 workflow gate / lint / CI

## 示範順序
### Step 1
人先寫一版 inventory 與 1 張 SCOPE card。

### Step 2
請 AI：
- 找遺漏 evidence
- 提出反例
- 指出哪裡太空泛
- 補一個 unseen task

### Step 3
請 AI 當 reviewer：
- 這條 convention 的邊界在哪？
- 哪裡 evidence 不夠？
- 哪裡只是個案，不是規則？
- 哪裡雖然格式對，但仍不貼近本 repo / 文件集？

### Step 4
用 TRACE 做最後判斷。

## 示範收束句
不是叫 AI 直接幫你定規則。
是先用人類方法抽出規則，再叫 AI 幫你檢查這條規則是否真的站得住。
