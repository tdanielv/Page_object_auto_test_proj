import time
import webbrowser

import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from .pages.locators import Cart_Page_Locators
from .pages.login_page import Login_Page
from .pages.main_page import Main_Page
from .pages.test_product_page import Product_Page

link_main_page = "http://selenium1py.pythonanywhere.com/"
login_link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
# product_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
#
# def test_guest_can_go_to_login_page(browser):
#     page = Main_Page(browser, link_main_page)
#     page.open()
#     page.got_to_login_page()
#     login_page = Login_Page(browser, browser.current_url)
#     login_page.should_be_login_page()
#
# def test_guest_should_see_login_link(browser):
#     page = Main_Page(browser, link_main_page)
#     page.open()
#     page.should_be_login_link()
#
# def test_there_is_login_form(browser):
#     testing = Login_Page(browser, login_link)
#     testing.open()
#     testing.should_be_login_form()
#
# def test_there_is_register_form(browser):
#     testing = Login_Page(browser, login_link)
#     testing.open()
#     testing.should_be_register_form()
#
# def test_login_url_is_good(browser):
#     testing = Login_Page(browser, login_link)
#     testing.open()
#     testing.should_be_login_url()

# @pytest.mark.parametrize('number', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
# @pytest.mark.parametrize('number', ['7', '8', '9'])
@pytest.mark.parametrize('number', ['0', '1', '2', '3', '4', '5', '6', pytest.param("7", marks=pytest.mark.xfail), '8', '9'])
def test_guest_can_add_product_to_basket(browser, number):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}'
    page = Product_Page(browser, link)
    page.open()
    name = page.add_item_into_cart()
    page.solve_quiz_and_get_code()
    page.add_to_cart_is_succesfull(name)



