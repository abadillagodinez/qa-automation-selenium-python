from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DepartmentListPage:

    # Locators for elements on the department list page
    TD_EMPTY = (By.XPATH, "//td[text()='No departments found. Add a new one!']")

    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        self.driver.get("http://localhost:5173/")
        # wait to DOM for load
        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )

    def get_empty_td_text(self):
        # Wait for the empty TD element to be present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TD_EMPTY)
        )
        return self.driver.find_element(*self.TD_EMPTY).text