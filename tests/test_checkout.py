import pytest
import logging
from pages.checkout_page import CheckoutPage
from utils.data_loader import get_csv_data

# 1. 讀取外部測試資料 (SKU, 數量, 預期價格)
# 假設 csv 內容: product_name,qty,expected_price
TEST_DATA = get_csv_data("checkout_data.csv")

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
@pytest.mark.parametrize("data", TEST_DATA)
async def test_checkout_process(authenticated_page, data):
    """
    測試結帳流程 (使用 authenticated_page fixture 自動登入)
    """
    # Arrange (準備資料)
    product_name = data['product_name']
    qty = int(data['qty'])
    expected_price = int(data['expected_price'])
    
    checkout_page = CheckoutPage(authenticated_page)
    
    # Act (執行動作)
    # 1. 搜尋並加購物車
    await checkout_page.search_and_add_item(product_name, qty)
    
    # 2. 前往結帳
    await checkout_page.proceed_to_checkout()
    
    # 3. 獲取金額
    actual_price = await checkout_page.get_final_price()
    
    # Assert (驗證結果)
    logger.info(f"Verifying price: Expected {expected_price}, Got {actual_price}")
    
    assert actual_price == expected_price, \
        f"❌ 價格錯誤! 預期: {expected_price}, 實際: {actual_price}"
