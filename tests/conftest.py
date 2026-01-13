import pytest
import os
from playwright.async_api import async_playwright
from pages.login_page import LoginPage # 引用您原本有的 login_page

# 假定 .env 有設定測試帳號
TEST_USER = os.getenv("TEST_USER", "demo@example.com")
TEST_PWD = os.getenv("TEST_PWD", "123456")

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """設定瀏覽器 Context (如視窗大小、語系)"""
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "locale": "zh-TW"
    }

@pytest.fixture(scope="function")
async def authenticated_page(page):
    """
    [高階技巧] 自動登入的 Fixture
    任何測試函式只要參數寫 'authenticated_page'，
    就會獲得一個已經登入好的 page 物件。
    """
    login_page = LoginPage(page)
    
    # 1. 前往首頁
    await page.goto("/") 
    
    # 2. 執行登入 (假設 LoginPage 有這個方法)
    # 這裡的邏輯可以改為檢查 storage_state 是否存在，若有直接 load，加速測試
    await login_page.navigate_to_login()
    await login_page.do_login(TEST_USER, TEST_PWD)
    
    # 3. 回傳已經登入的 page 給測試用
    yield page
