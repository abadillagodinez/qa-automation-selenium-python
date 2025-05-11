from pages.home_page import HomePage
import time

def test_open_homepage(driver):
    home = HomePage(driver)
    home.go_to()
    time.sleep(5)
    assert "Welcome to the-internet" in home.get_heading_text()
    home.click_Digest()