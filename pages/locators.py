from selenium.webdriver.common.by import By


class Main_Page_Locators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class Login_Page_Locators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')

class Cart_Page_Locators():
    TO_CART_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')

    NAME_ITEM = (By.CSS_SELECTOR, 'div.product_main >h1')
    NAME_ITEM_AFTER_CLICK = (By.CSS_SELECTOR, 'div.alertinner >strong')
    NAME_ITEM_IN_CART = (By.CSS_SELECTOR, 'div.row > div > h3 > a')

    PRICE_ITEM = (By.CSS_SELECTOR, 'div.product_main >p.price_color')
    PRICE_ITEM_AFTER_CLICK = (By.CSS_SELECTOR, 'div.alertinner > p >strong')
    PRICE_ITEM_IN_CART =(By.CSS_SELECTOR, 'p.price_color')

    CART_LINK = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')