# 電商核心流程 E2E 自動化測試框架 (Playwright)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Playwright](https://img.shields.io/badge/Playwright-1.40%2B-orange)
![Pytest](https://img.shields.io/badge/Pytest-7.0-yellow)
![Status](https://img.shields.io/badge/Status-Maintained-brightgreen)

## 專案簡介
本專案是針對**高併發電商交易系統**與**金融邏輯**設計的現代化 E2E (End-to-End) 自動化測試框架。

採用 **Playwright** 結合 **Python** 開發，解決了傳統工具（如 Selenium）在處理動態網頁時的不穩定問題。本框架嚴格遵循 **Page Object Model (POM)** 設計模式，並整合了 **MySQL 資料庫驗證**與 **Excel 資料驅動測試 (DDT)**，確保從前端 UI 操作到後端帳務紀錄的一致性與精準度。

---

## 核心技術特點

* ** 極致的穩定性 (Auto-wait 機制)：**
    利用 Playwright 內建的自動等待功能，徹底解決因網路延遲或網頁渲染未完成導致的測試誤判 (Flaky Tests)，無需再寫死 `sleep` 時間。
* ** 模組化架構設計 (POM)：**
    實作 Page Object Model，將「頁面元素定位」與「業務測試邏輯」完全分離。當 UI 改版時，僅需維護單一頁面物件，大幅降低維護成本。
* ** 網路攔截與 Mocking (Network Interception)：**
    利用 Playwright 攔截網路請求 (Network Requests)，可模擬第三方金流（如 LINE Pay）逾時或失敗的情境，驗證系統的錯誤處理機制。
* ** 資料驅動測試 (Data-Driven Testing)：**
    整合 `Pandas` 讀取 Excel/CSV 測試數據，透過參數化執行，單一腳本即可覆蓋多種邊界數據（例如：不同幣別、庫存臨界值）。
* ** UI 與 DB 雙重驗證 (Database Consistency)：**
    不只驗證畫面顯示成功，更在交易後自動連線 **MySQL** 資料庫，檢查訂單狀態與庫存扣減是否正確，防止帳務漏洞。
* ** 視覺化除錯 (Trace Viewer)：**
    測試失敗時自動保留完整的執行軌跡（包含截圖、錄影與網路封包），協助開發人員快速回放並定位問題。

---

## 🛠 技術棧

| 元件 | 使用工具 / 套件 | 用途說明 |
| :--- | :--- | :--- |
| **程式語言** | Python 3.9+ | 核心開發語言 |
| **自動化引擎** | **Playwright** | 新一代瀏覽器自動化工具 (支援 Chromium, Firefox, WebKit) |
| **測試執行器** | Pytest | 測試案例管理與 Fixture 實作 |
| **資料處理** | Pandas | 處理大量 Excel/CSV 測試資料 |
| **資料庫驗證** | PyMySQL | 連線資料庫進行 SQL 驗證 |
| **測試報告** | Allure Report | 產出包含截圖與圖表的視覺化報告 |
| **環境管理** | Python-dotenv | 管理敏感資訊 (如 DB 密碼)，確保資安 |

---

## 專案結構
本專案採用標準分層架構，確保高可讀性與擴充性：

```text
├── config/              # 全域設定檔 (Base URL, 瀏覽器參數, Timeout 設定)
├── pages/               # 頁面物件層 (POM) - 封裝定位器與操作方法
│   ├── base_page.py     # 封裝 Playwright 基礎方法 (封裝等待與例外處理)
│   ├── login_page.py    # 登入頁面邏輯
│   └── checkout_page.py # 結帳與交易流程邏輯
├── tests/               # 測試腳本層 (Test Scripts) - 撰寫業務邏輯與斷言
│   ├── conftest.py      # Pytest Fixtures (設定瀏覽器環境、登入狀態共用)
│   ├── test_login.py
│   └── test_checkout.py
├── test_data/           # 測試資料 (存放 Excel/CSV 檔案)
├── utils/               # 工具庫 (DB 連線器, API 輔助工具)
├── requirements.txt     # 專案套件依賴清單
├── pytest.ini           # Pytest 設定檔
└── README.md            # 專案說明文件
