from .base_page import Base_Page
from .locators import Login_Page_Locators, Registration_Form_Locators


class Login_Page(Base_Page):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        assert self.is_element_present(*Login_Page_Locators.LOGIN_FORM), 'Login form is not found'

    def should_be_register_form(self):
        assert self.is_element_present(*Login_Page_Locators.REGISTER_FORM), 'Register form is not found'

    def should_be_login_url(self):
        link_text = self.browser.current_url
        assert 'login' in link_text, 'Error'

    def register_new_user(self, email, password):
        mail = self.browser.find_element(*Registration_Form_Locators.EMAIL)
        mail.send_keys(email)
        password1 = self.browser.find_element(*Registration_Form_Locators.PASSWORD)
        password1.send_keys(password)
        password2 = self.browser.find_element(*Registration_Form_Locators.PASSWORD2)
        password2.send_keys(password)
        self.browser.find_element(*Registration_Form_Locators.REGISTER_BUTTON).click()

