from playwright.async_api import Page, Locator, expect
import logging

logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    async def navigate(self, path: str = ""):
        url = f"{path}"
        logger.info(f"Navigating to: {url}")
        await self.page.goto(url)

    async def click_element(self, locator: Locator):
        try:
            await locator.wait_for(state="visible")
            await locator.highlight() # Playwright 內建的高亮功能
            await locator.click()
        except Exception as e:
            logger.error(f"Click failed on {locator}: {e}")
            raise
