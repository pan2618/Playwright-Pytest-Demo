import pytest
import allure
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from utils.data_loader import load_csv_data
from config.settings import Settings

# 從 CSV 讀取資料
TEST_DATA = load_csv_data("data/test_orders.csv")

@allure.feature("Core Transaction Flow")
@allure.story("Checkout with multiple scenarios")
@pytest.mark.parametrize("order_data", TEST_DATA)
@pytest.mark.asyncio
async def test_end_to_end_checkout(page, order_data):
    """
    驗證端對端購物流程：
    1. 登入
    2. 搜尋商品 (參數化)
    3. 加入購物車 (參數化)
    4. 結帳並驗證金額
    """
    # Arrange
    login_page = LoginPage(page)
    checkout_page = CheckoutPage(page)
    
    sku = order_data['sku']
    qty = order_data['qty']
    expected_total = order_data['expected_total']

    # Act
    await login_page.navigate(Settings.BASE_URL)
    await login_page.login(Settings.USERNAME, Settings.PASSWORD)
    
    with allure.step(f"Search and add product {sku} x {qty}"):
        await checkout_page.search_and_add_to_cart(sku, qty)
    
    with allure.step("Proceed to checkout"):
        final_price = await checkout_page.get_cart_total()

    # Assert
    with allure.step("Verify Price Accuracy"):
        # 資深細節：處理浮點數運算誤差
        assert float(final_price) == float(expected_total), \
            f"Price mismatch! Expected {expected_total}, got {final_price}"
