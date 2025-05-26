from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# the page class
class W3sPage:

    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        w3school_url = "https://www.w3schools.com/bootstrap/bootstrap_carousel.asp"
        self.driver.get(w3school_url)

        # wait DOM to load
        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )

    def scroll_into_carousel(self):
        # xpath
        carousel_title_xpath = "//h2[text()='Carousel Example']"
        # get the title
        carousel_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, carousel_title_xpath))
        )
        # get the position y for the title
        carousel_title_y = carousel_title.location["y"]
        # execute js script to get the sum of the both nav elements height
        header_height = self.driver.execute_script("""
            let pagetop = document.getElementById('pagetop')?.offsetHeight || 0;
            let subtopnav = document.getElementById('subtopnav')?.offsetHeight || 0;
            return pagetop + subtopnav;
        """)
        # execute the js script to scroll
        self.driver.execute_script(f"window.scrollTo(0,{carousel_title_y-header_height})")

    def is_carousel_visible(self):
        carousel_xpath = "//div[@id='myCarousel']"
        carousel = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, carousel_xpath))
        )
        if carousel is not None:
            return True
        else:
            return False
        
    def get_active_slide(self, active_xpath):
        active = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,active_xpath))
        )
        return active
        
    # function to check the slide is active
    def slide_is_active(self, active_xpath, slides, i):
        active = self.driver.find_elements(By.XPATH, active_xpath)
        return len(active) == 1 and active[0] == slides[i]

    def test_click_dots(self):
        # xpath
        dots_xpath = "//li[@data-target='#myCarousel']"
        slides_xpath = "//div[@class='carousel-inner']//div[contains(@class,'item')]"

        # get the elements
        dots = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, dots_xpath))
        )
        slides = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, slides_xpath))
        )

        # if both appears
        if (dots is not None) and (slides is not None):
            # xpath for active slide
            active_xpath = "//div[@class='carousel-inner']//div[contains(@class,'item') and contains(@class,'active')]"
            # for each dot in the dots
            for i, dot in enumerate(dots):
                dot.click()
                
                # wait until slide is active
                WebDriverWait(self.driver, 10).until(
                    lambda driver: self.slide_is_active(active_xpath, slides, i)
                )

                # get the active slide
                active_slide = self.get_active_slide(active_xpath)
                expected_slide = slides[i]

                # Comparar por alguna propiedad estable, como el texto o posición
                assert active_slide.text == expected_slide.text, f"Active slide isn´t the correct for dot {i}"

    def test_click_arrows(self):
        # xpath
        arrows_xpath = "//a[@role='button' and contains(@class,'carousel-control')]"
        slides_xpath = "//div[@class='carousel-inner']//div[contains(@class,'item')]"

        arrows = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, arrows_xpath))
        )
        slides = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, slides_xpath))
        )
        if(arrows is not None) and (slides is not None):
            left = arrows[0]
            right = arrows[1]
            active_xpath = "//div[@class='carousel-inner']//div[contains(@class,'item') and contains(@class,'active')]"
            previous_click_value = self.get_active_slide(active_xpath)
            right.click()
            time.sleep(3)
            post_click_value = self.get_active_slide(active_xpath)
            left.click()
            time.sleep(3)
            actual_click_value = self.get_active_slide(active_xpath)
            
            assert previous_click_value.text == actual_click_value.text, "The arrows of the carrousel are not moving properly"


            
