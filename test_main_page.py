from selenium.webdriver.common.by import By
from .pages.login_page import Login_Page
from .pages.main_page import Main_Page

link_main_page = "http://selenium1py.pythonanywhere.com/"
login_link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'

def test_guest_can_go_to_login_page(browser):
    page = Main_Page(browser, link_main_page)
    page.open()
    page.got_to_login_page()

def test_guest_should_see_login_link(browser):
    page = Main_Page(browser, link_main_page)
    page.open()
    page.should_be_login_link()

def test_there_is_login_form(browser):
    testing = Login_Page(browser, login_link)
    testing.open()
    testing.should_be_login_form()

def test_there_is_register_form(browser):
    testing = Login_Page(browser, login_link)
    testing.open()
    testing.should_be_register_form()

def test_login_url_is_good(browser):
    testing = Login_Page(browser, login_link)
    testing.open()
    testing.should_be_login_url()


