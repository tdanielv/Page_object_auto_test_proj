from Page_object_auto_test_proj.pages.base_page import Base_Page
from Page_object_auto_test_proj.pages.locators import Cart_Page_Locators


class Basket_Page(Base_Page):
    def click_to_button_cart(self):
        self.browser.find_element(*Cart_Page_Locators.CART_LINK).click()\

    def cart_is_empty(self):
        print(self.browser.find_element(*Cart_Page_Locators.CART_LIST_TEXT).text)
        assert 'Ваша корзина пуста' in self.browser.find_element(*Cart_Page_Locators.CART_LIST_TEXT).text, 'Cart is not empty'
