from playwright.async_api import Page, expect
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)

class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Selectors (定義區)
        self.search_input = page.get_by_placeholder("搜尋商品...") # 假設
        self.search_btn = page.get_by_role("button", name="搜尋")
        self.add_to_cart_btn = page.get_by_role("button", name="加入購物車")
        self.cart_icon = page.locator(".cart-icon") # 假設
        self.checkout_btn = page.get_by_role("button", name="前往結帳")
        
        # 價格顯示元素 (假設 class)
        self.total_price_text = page.locator(".total-price")

    async def search_and_add_item(self, keyword: str, qty: int = 1):
        """搜尋商品並加入購物車"""
        logger.info(f"Searching for product: {keyword}")
        
        # 1. 搜尋
        await self.search_input.fill(keyword)
        await self.search_btn.click()
        
        # 2. 點擊進入商品詳情 (或是直接在列表頁加購物車)
        # 這裡假設點擊第一個搜尋結果
        await self.page.locator(".product-item").first.click()
        
        # 3. 加入購物車 (處理數量)
        # 如果有數量選擇器，需在此處理，這裡簡化為直接點擊
        for _ in range(int(qty)):
             await self.add_to_cart_btn.click()
        
        logger.info(f"Added {qty} item(s) to cart.")

    async def proceed_to_checkout(self):
        """進入結帳頁面"""
        await self.cart_icon.click()
        await expect(self.checkout_btn).to_be_visible()
        await self.checkout_btn.click()

    async def get_final_price(self) -> int:
        """獲取結帳頁面的最終金額 (去除 '$' 與 ',' 符號)"""
        await expect(self.total_price_text).to_be_visible()
        price_str = await self.total_price_text.text_content()
        # 清理字串: "$1,200" -> 1200
        clean_price = price_str.replace("$", "").replace(",", "").strip()
        return int(clean_price)
