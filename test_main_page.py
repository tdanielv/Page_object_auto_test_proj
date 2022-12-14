import time
import webbrowser

import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from .pages.basket_page import Basket_Page
from .pages.locators import Cart_Page_Locators, ProductPageLocators
from .pages.login_page import Login_Page
from .pages.main_page import Main_Page
from .pages.product_page import Product_Page

link_main_page = "http://selenium1py.pythonanywhere.com/"
login_link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'


@pytest.mark.login_guest
class TestLoginFromMainPAge():
    # @pytest.mark.skip(reason='its done')
    def test_login_url_is_good(self, browser):
        testing = Login_Page(browser, login_link)
        testing.open()
        testing.should_be_login_url()

    # @pytest.mark.skip(reason='its done')
    def test_guest_can_go_to_login_page(self, browser):
        page = Main_Page(browser, link_main_page)
        page.open()
        page.got_to_login_page()
        login_page = Login_Page(browser, browser.current_url)
        login_page.should_be_login_page()

    # @pytest.mark.skip(reason='its done')
    def test_guest_should_see_login_link(self, browser):
        page = Main_Page(browser, link_main_page)
        page.open()
        page.should_be_login_link()

    # @pytest.mark.skip(reason='its done')
    def test_there_is_login_form(self, browser):
        testing = Login_Page(browser, login_link)
        testing.open()
        testing.should_be_login_form()

# @pytest.mark.skip(reason='its done')
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = Basket_Page(browser, link_main_page)
    page.open()
    page.click_to_button_cart()
    page.cart_is_empty()

# @pytest.mark.skip(reason='its done')
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = Product_Page(browser, link)
    page.open()
    page.should_be_login_link()

# @pytest.mark.skip(reason='its done')
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = Product_Page(browser, link)
    page.open()
    page.got_to_login_page()





# @pytest.mark.skip(reason='its done')
def test_there_is_register_form(browser):
    testing = Login_Page(browser, login_link)
    testing.open()
    testing.should_be_register_form()







