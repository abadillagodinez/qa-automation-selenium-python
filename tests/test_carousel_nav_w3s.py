import pytest
from pages.w3school_page import W3sPage
import time

def test_carousel_nav_w3s(driver):

    w3sPage = W3sPage(driver)

    w3sPage.go_to()
    assert "Bootstrap Carousel" in driver.title, "Seems that the page open is not the Bootstrap Carousel tutorial page"

    w3sPage.scroll_into_carousel()
    assert w3sPage.is_carousel_visible(), "Carousel is not visible"

    w3sPage.test_click_dots()

    w3sPage.test_click_arrows()
