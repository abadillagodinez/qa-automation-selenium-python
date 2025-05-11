from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        self.driver.get("https://the-internet.herokuapp.com")

    def get_heading_text(self):
        return self.driver.find_element(By.TAG_NAME, "h1").text
    
    def click_Digest(self):
        xpath = "//a[text()='Digest Authentication']"
        button = self.driver.find_element(By.XPATH, xpath)
        button.click()

    