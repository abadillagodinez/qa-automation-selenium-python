import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
import time

@pytest.fixture
def driver():
    service = FirefoxService(GeckoDriverManager().install())
    options = webdriver.FirefoxOptions()
    ## options.add_argument("--headless")
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()