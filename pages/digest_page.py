from selenium.webdriver.common.by import By
import json
import os

class DigestPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
        credentials_path = os.path.join(base_dir, 'credentials.json')
        with open(credentials_path) as f:
            creds = json.load(f)

        usuario = creds["usuario"]
        password = creds["password"]
        auth_url = f"https://{usuario}:{password}@the-internet.herokuapp.com/digest_auth"
        self.driver.get(auth_url)

    def get_heading3_text(self):
        return self.driver.find_element(By.TAG_NAME, "h3").text

    