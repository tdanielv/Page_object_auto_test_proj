from selenium.webdriver.common.by import By


class Main_Page_Locators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class Login_Page_Locators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')

class Cart_Page_Locators():
    TO_CART_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')