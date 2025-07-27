# mini-ir-register-allocator

## 專案簡介

本專案實作 IR（中間表示）的暫存器分配器，涵蓋兩種經典的 Register Allocation（RA）核心演算法：
- **Graph Coloring Register Allocation**
- **Linear Scan Register Allocation**

目前主體以 Linear Scan Register Allocation（線性掃描分配）為主，驗證其在三地址碼IR上的分配效益，目的是理解並掌握主流編譯器後端的分配策略及其工程應用。

---

## 目錄

- [專案簡介](#專案簡介)
- [理論背景與演算法說明](#理論背景與演算法說明)
  - [Graph Coloring Register Allocation](#graph-coloring-register-allocation)
  - [Linear Scan Register Allocation](#linear-scan-register-allocation)
  - [演算法比較](#演算法比較)
- [數據結構設計](#數據結構設計)
- [流程圖](#流程圖)
- [時空複雜度分析](#時空複雜度分析)
- [實作說明](#實作說明)
- [測試與執行結果](#測試與執行結果)
- [效益與侷限性分析](#效益與侷限性分析)
- [參考文獻](#參考文獻)

---

## 理論背景與演算法說明

### Graph Coloring Register Allocation

**原理**  
將每個變數於程式中的活躍區間視為圖的節點，若兩變數同時活躍則相連，轉化為圖著色問題。每種顏色代表一個寄存器，兩相鄰變數不得分配同一寄存器。

**核心流程**  
1. 活躍區間分析，建立干涉圖（Interference Graph）
2. 對圖進行著色（Graph Coloring）：分配寄存器
3. 若寄存器數不足，選擇變數 Spill（寫回記憶體）
4. 重新分析並分配，直到所有變數分配完畢

**優點**：分配品質高，能有效減少 spill  
**缺點**：演算法複雜度高，效率較低，不適合JIT/即時場景

---

### Linear Scan Register Allocation

**原理**  
先根據變數活躍區間的起點排序，線性掃描每個活躍區間，分配可用暫存器，遇到衝突時根據規則選擇變數spill至記憶體。

**核心流程**  
1. 計算每個變數的活躍區間（start, end）
2. 按起點排序
3. 掃描每個interval，開始時嘗試分配暫存器
4. 超過暫存器上限時選擇spill
5. 結束時釋放暫存器

**優點**：效率高（O(n)），結構簡單，適合JIT與即時編譯  
**缺點**：分配品質較低於圖著色，spill次數略多

---

### 演算法比較

| 項目         | Graph Coloring           | Linear Scan         |
|--------------|-------------------------|---------------------|
| 複雜度       | O(n^2)~O(n^3)           | O(n)                |
| 分配品質     | 高（較少spill）         | 中（可能多spill）   |
| 適用場合     | 靜態編譯                | JIT/即時編譯        |
| 實作難度     | 高                      | 低~中               |

---

## 數據結構設計

- **變數活躍區間（Live Interval）**  
  Python 字典格式：`{變數名: [start, end]}`
- **暫存器池（Registers）**  
  List格式：`['R1', 'R2', ...]`
- **Active List**  
  紀錄目前分配中的interval，便於即時檢查寄存器使用狀態

---

## 流程圖

#### Linear Scan Register Allocation 流程圖

```mermaid
graph TD
    A[開始] --> B[計算所有變數的活躍區間]
    B --> C[依起點排序intervals]
    C --> D{interval開始}
    D -->|active未滿| E[分配暫存器]
    D -->|active已滿| F[選一個spill到記憶體]
    E --> G[active加入interval]
    F --> G
    G --> H{interval結束}
    H -->|是| I[釋放暫存器]
    H -->|否| C
    I --> C
