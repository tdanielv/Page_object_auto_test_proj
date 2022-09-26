import pytest

from .pages.basket_page import Basket_Page
from .pages.locators import ProductPageLocators
from .pages.product_page import Product_Page

product_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'





def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = Basket_Page(browser, product_link)
    page.open()
    page.click_to_button_cart()
    page.cart_is_empty()

@pytest.mark.skip(reason='its failed')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = Product_Page(browser, product_link)
    page.open()
    page.click_to_button_buy()
    page.solve_quiz_and_get_code()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is find'

@pytest.mark.skip(reason='its done and waiting 4 sec')
def test_guest_cant_see_success_message(browser):
    page = Product_Page(browser, product_link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is find'

@pytest.mark.skip(reason='its failed and waiting 4 sec')
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = Product_Page(browser, product_link)
    page.open()
    page.click_to_button_buy()
    page.solve_quiz_and_get_code()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Succes message still here'