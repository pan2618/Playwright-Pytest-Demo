import pytest
import allure
from playwright.async_api import Page
from datetime import datetime

@pytest.fixture(scope="function", autouse=True)
async def screenshot_on_failure(request, page: Page):
    """
    全域 Fixture：當測試失敗時，自動截圖並掛載到 Allure 報告中
    """
    yield # 測試執行點
    
    # 如果測試結果為 failed
    if request.node.rep_call.failed:
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_path = f"reports/screenshots/fail_{timestamp}.png"
        
        await page.screenshot(path=screenshot_path, full_page=True)
        
        # 附加到 Allure 報告
        allure.attach.file(
            screenshot_path, 
            name="Failure Screenshot", 
            attachment_type=allure.attachment_type.PNG
        )
