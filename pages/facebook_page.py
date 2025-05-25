from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# the class for the test_login_facebook file
class FacebookPage:
    # the constructor
    def __init__(self, driver):
        self.driver = driver

    # method to load the page
    def go_to(self):
        facebook_url = "https://www.facebook.com"
        self.driver.get(facebook_url)
        
        # wait to DOM for load
        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )

    # method to enter the credentials
    def enter_credentials(self, user, password):

        # xpaths for input fields
        user_input_xpath = "//input[@id='email']"
        pass_input_xpath = "//input[@id='pass']"

        # get the web elements
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, user_input_xpath))
        ).send_keys(user)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, pass_input_xpath))
        ).send_keys(password)
    
    # method to click login button
    def click_login(self):
        login_button_xpath = "//button[@name='login']"
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, login_button_xpath))
        ).click()

    # method to get the title of the page
    def get_page_title(self):
        return self.driver.title
    
    # method to get the url of the page
    def get_current_url(self):
        return self.driver.current_url
    
    # method to confirm credentials were wrong
    def was_the_wrong_credentials(self):
        # xpath for the wrong credentials div
        incorrect_eamil_xpath = "//div[contains(text(), 'Wrong Credentials')]"
        # wait for the element
        incorrect_email_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, incorrect_eamil_xpath))
        )
        # if the element appear return true
        if incorrect_email_message is not None:
            return True
        else:
            return False
        
    # method to confirm that the inputs were 
    def were_inputs_empty(self):
        # xpaths for input fields
        email_input_xpath = "//input[@id='email']"
        pass_input_xpath = "//input[@id='pass']"

        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, email_input_xpath))
        )
        pass_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, pass_input_xpath))
        )

        # if both input fields are there
        if ((email_input is not None) and (pass_input is not None)):
            # if both values are empty return true
            if email_input.get_attribute("value") == "" and pass_input.get_attribute("value") == "":
                return True
            else:
                return False