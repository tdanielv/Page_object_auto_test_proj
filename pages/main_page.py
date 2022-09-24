from selenium.webdriver.common.by import By
from .base_page import Base_Page

class Main_Page(Base_Page):

    def got_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, '#login_link')
        login_link.click()