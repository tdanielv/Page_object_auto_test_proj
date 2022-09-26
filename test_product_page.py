import time

import pytest

from .pages.basket_page import Basket_Page
from .pages.locators import ProductPageLocators
from .pages.login_page import Login_Page
from .pages.product_page import Product_Page
from .test_main_page import link_main_page

product_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self,browser):
        page = Product_Page(browser, product_link)
        page.open()
        page.got_to_login_page()
        login_page = Login_Page(browser, browser.current_url)
        email = str(time.time()) + '@fakemail.ru'
        login_page.register_new_user(email, 'Asdfghjkl1_')
        login_page.should_be_authorized_user()
        yield browser

    # @pytest.mark.skip(reason='its done')
    # @pytest.mark.parametrize('number', ['0', '1', '2', '3', '4', '5', '6', pytest.param("7", marks=pytest.mark.xfail), '8', '9'])
    @pytest.mark.parametrize('number', ['0'])
    def test_user_can_add_product_to_basket(self, browser, number):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}'
        page = Product_Page(browser, link)
        page.open()
        page.add_to_shopping_cart()
        page.should_be_after_adding_to_cart()

    @pytest.mark.skip(reason='its done and waiting 4 sec')
    def test_user_cant_see_success_message(self, browser):
        page = Product_Page(browser, product_link)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is find'

    @pytest.mark.skip(reason='its failed')
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = Product_Page(browser, product_link)
        page.open()
        page.click_to_button_buy()
        page.solve_quiz_and_get_code()
        assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is find'

    @pytest.mark.skip(reason='its done')
    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = Basket_Page(browser, product_link)
        page.open()
        page.click_to_button_cart()
        page.cart_is_empty()

    @pytest.mark.skip(reason='its failed and waiting 4 sec')
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = Product_Page(browser, product_link)
        page.open()
        page.click_to_button_buy()
        page.solve_quiz_and_get_code()
        assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Succes message still here'

@pytest.mark.need_review
@pytest.mark.parametrize('number', ['0'])
def test_guest_can_add_product_to_basket( browser, number):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}'
    page = Product_Page(browser, link)
    page.open()
    page.add_to_shopping_cart()
    page.should_be_after_adding_to_cart()
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = Basket_Page(browser, link_main_page)
    page.open()
    page.click_to_button_cart()
    page.cart_is_empty()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = Product_Page(browser, link)
    page.open()
    page.got_to_login_page()