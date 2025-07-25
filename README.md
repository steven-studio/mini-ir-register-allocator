# mini-ir-register-allocator

一個用 Python 製作的簡易編譯器 IR（中間碼）與 Register Allocation（暫存器分配）示範專案。  
本專案以最小原型實現三地址碼產生、活躍區間分析、干擾圖建構、以及圖著色暫存器分配等現代編譯器核心步驟。  
適合初學者學習編譯器底層原理、驗證 register allocation 流程。

---

## 專案結構

mini-ir-register-allocator/
├── main.py              # 專案主程式
├── ir_generator.py      # IR（三地址碼）產生
├── liveness.py          # 活躍區間分析
├── reg_alloc.py         # 干擾圖建構與暫存器分配
└── sample_input.txt     # 範例輸入程式

---

## 使用說明

1. **安裝需求**  
   本專案僅需 Python 3，無外部依賴。

2. **執行步驟**  
   - 將你的原始程式碼（簡單賦值/運算）寫入 `sample_input.txt`
   - 在終端機執行：
     ```
     python3 main.py
     ```
   - 範例輸出將包含：
     - IR（三地址碼）清單
     - 各變數活躍區間
     - 干擾圖結構
     - 暫存器分配結果

3. **測試範例**

   `sample_input.txt` 內容：

a = 1
b = 2
c = a + b
d = c * 5
return d

執行結果：

IR: [‘a = 1’, ‘b = 2’, ‘c = a + b’, ‘d = c * 5’, ‘return d’]
Live Ranges: {‘a’: [0, 2], ‘b’: [1, 2], ‘c’: [2, 3], ‘d’: [3, 4]}
Register Mapping: {‘a’: ‘R1’, ‘b’: ‘R2’, ‘c’: ‘R3’, ‘d’: ‘R1’}

---

## 專案特色

- 完整展示 IR 到 Register Allocation 的基本流程
- 代碼簡明，易於二次開發與教學
- 支援活躍區間/干擾圖/圖著色核心步驟
- 適合用於課程、演示或個人編譯器練習起步

---

## 後續可擴充方向

- 自動將高階語法轉換為三地址碼
- 支援更複雜語法與流程控制（如 if、while）
- 加入 SSA、CFG 結構
- 編寫單元測試與錯誤處理

---

## 聯絡與貢獻

如有建議、回饋或 Pull Request，歡迎在 GitHub 提出。

---

**本專案僅供教學與學習交流使用，不適用於生產環境。**


