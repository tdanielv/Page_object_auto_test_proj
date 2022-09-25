from selenium.webdriver.common.by import By
from .base_page import Base_Page
from .locators import Main_Page_Locators
from .login_page import Login_Page

class Main_Page(Base_Page):

    def got_to_login_page(self):
        login_link = self.browser.find_element(*Main_Page_Locators.LOGIN_LINK)
        login_link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*Main_Page_Locators.LOGIN_LINK), 'Login link is not presented'