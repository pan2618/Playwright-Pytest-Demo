import pytest
from pages.google_home_page import GoogleHomePage
from pages.google_results_page import GoogleResultsPage

def test_Google_Search_with_POM(driver):
    home_page = GoogleHomePage(driver)
    home_page.search_for("Selenium")
    results_page = GoogleResultsPage(driver)
    page_title = results_page.get_title()
    assert "Selenium" in page_title, "頁面標題未包含 'Selenium'！"