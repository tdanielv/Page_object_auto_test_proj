from selenium.webdriver.common.by import By

from .pages.main_page import Main_Page

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = Main_Page(browser, link)
    page.open()
    page.got_to_login_page()


