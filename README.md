# 🛒 E-Commerce & Financial Transaction Automation Framework

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.0-green)
![Pytest](https://img.shields.io/badge/Pytest-7.0-yellow)
![Status](https://img.shields.io/badge/Status-Maintained-brightgreen)

## 📖 Project Overview (專案簡介)
This project is a robust **End-to-End (E2E) Automation Testing Framework** designed to simulate complex business scenarios in e-commerce and financial transaction systems. 

It adopts the **Page Object Model (POM)** design pattern to ensure scalability and maintainability. Beyond standard UI interactions, this framework integrates **Database Verification (SQL)** and **Data-Driven Testing (DDT)** to guarantee data integrity and transaction accuracy—critical standards for the fintech industry.

(本專案為基於 POM 設計模式開發的 E2E 自動化測試框架。除了 UI 驗證外，特別整合了 MySQL 資料庫核對與 Excel 數據驅動測試，確保交易資料的一致性與精準度。)

---

## 🚀 Key Features (核心特點)

* **🏗 Modular Architecture (POM):** Separates page locators from test logic. Maintenance effort reduced by 60% when UI changes.
* **📊 Data-Driven Testing (DDT):** Utilizes `Pandas` to load test data from Excel/CSV, enabling high-coverage testing (e.g., various currency inputs, inventory edge cases).
* **🔐 Database Verification:** Integrated `PyMySQL` to verify transaction records and inventory deduction in the DB directly after UI actions.
* **🛡 Stability & Resilience:** Implemented `Explicit Waits` and retry mechanisms to handle network latency and prevent flaky tests.
* **📈 Visual Reporting:** Integrated **Allure Report** to generate detailed test execution logs and screenshots for debugging.
* **⚙️ Environment Management:** Uses `requirements.txt` and `.env` for consistent dependency and configuration management across CI/CD pipelines.

---

## 🛠 Tech Stack (技術架構)

| Component | Tool / Library | Usage |
| :--- | :--- | :--- |
| **Language** | Python 3.9+ | Core programming language |
| **Web Automation** | Selenium WebDriver 4 | Browser interaction |
| **Test Runner** | Pytest | Test execution and fixture management |
| **Data Processing** | Pandas | Reading test data from Excel/CSV |
| **Database** | PyMySQL / SQLAlchemy | SQL verification |
| **Reporting** | Allure / Pytest-html | Visualization of test results |
| **Config** | Python-dotenv | Managing sensitive credentials |

---

## 📂 Project Structure (專案結構)

```text
├── config/              # Global configurations (URL, DB params, Timeout settings)
├── pages/               # Page Object Model (POM) classes - Locators & Methods
│   ├── base_page.py     # Common methods (click, type, wait)
│   ├── login_page.py    # Login business logic
│   └── checkout_page.py # Transaction logic
├── tests/               # Test scripts (Business Logic)
│   ├── test_login.py
│   └── test_checkout.py
├── test_data/           # Excel/CSV files for Data-Driven Testing
├── utils/               # Helper functions (DB connector, Logger)
├── requirements.txt     # Project dependencies
├── pytest.ini           # Pytest configuration
└── README.md            # Project documentation
