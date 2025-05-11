from pages.digest_page import DigestPage
import time

def test_open_homepage(driver):
    digest = DigestPage(driver)
    digest.go_to()
    time.sleep(5)
    assert "Digest Auth" in digest.get_heading3_text()
