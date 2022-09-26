import math
import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from .base_page import Base_Page
from .locators import Cart_Page_Locators, ProductPageLocators


class Product_Page(Base_Page):
    def add_item_into_cart(self):
        price_item = self.browser.find_element(*Cart_Page_Locators.PRICE_ITEM).text
        name_item = self.browser.find_element(*Cart_Page_Locators.NAME_ITEM).text
        if self.is_element_present(*Cart_Page_Locators.TO_CART_BUTTON):
            self.browser.find_element(*Cart_Page_Locators.TO_CART_BUTTON).click()
        return name_item

    def add_to_shopping_cart(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        btn.click()
        self.solve_quiz_and_get_code()

    def should_be_after_adding_to_cart(self):
        self.should_be_correct_name_of_good_in_cart()
        self.should_be_correct_price_of_good_in_cart()

    def add_to_cart_is_succesfull(self, name_item):
        name_item_after_click = self.browser.find_element(*Cart_Page_Locators.NAME_ITEM_AFTER_CLICK).text
        price_item_after_click = self.browser.find_element(*Cart_Page_Locators.PRICE_ITEM_AFTER_CLICK).text
        self.browser.find_element(*Cart_Page_Locators.CART_LINK).click()
        price_cart_item = self.browser.find_element(*Cart_Page_Locators.PRICE_ITEM_IN_CART).text
        name_cart_item = self.browser.find_element(*Cart_Page_Locators.NAME_ITEM_IN_CART).text
        # if name_item != name_item_after_click:
        #     print('Error in name')
        assert name_item==name_item_after_click, 'errorroroergoergwpmrgpwmge'

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert

            alert_text = alert.text
            print(f"Your code: {alert_text}")

            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")\


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def click_to_button_buy(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_BUY).click()

    def should_be_correct_name_of_good_in_cart(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_OF_GOOD_IN_ALERT).text \
               == self.browser.find_element(*ProductPageLocators.NAME_OF_GOOD).text, \
            "The name of the product in the alert does not match the real name of the product!"

    def should_be_correct_price_of_good_in_cart(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_OF_GOOD_IN_ALERT).text \
               == self.browser.find_element(*ProductPageLocators.PRICE_OF_GOOD).text, \
            "The price of the product in the basket does not match the real price of the product!"

