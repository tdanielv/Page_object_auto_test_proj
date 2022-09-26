from selenium.webdriver.common.by import By
from .base_page import Base_Page
from .locators import Main_Page_Locators, Cart_Page_Locators
from .login_page import Login_Page

class Main_Page(Base_Page):

    def __init__(self, *args, **kwargs):
        super(Main_Page, self).__init__(*args, **kwargs)

