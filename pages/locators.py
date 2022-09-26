from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')

class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner')
    BUTTON_BUY = (By.CSS_SELECTOR, 'button.btn-add-to-basket')

    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_OF_GOOD = (By.CSS_SELECTOR, ".product_main > .price_color")
    NAME_OF_GOOD = (By.CSS_SELECTOR, ".product_main > h1")
    NAME_OF_GOOD_IN_ALERT = (By.CSS_SELECTOR, "#messages > :nth-child(1) strong")
    PRICE_OF_GOOD_IN_ALERT = (By.CSS_SELECTOR, "#messages > :nth-child(3) strong")

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

    CART_LINK = (By.CSS_SELECTOR, 'span.btn-group > a.btn.btn-default')

    CART_LIST_TEXT = (By.ID, 'content_inner')
    # div.basket-items

class Registration_Form_Locators():
    EMAIL = (By.ID, 'id_registration-email')
    PASSWORD = (By.ID, 'id_registration-password1')
    PASSWORD2 = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button.btn[value="Register"]')



























class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BTN_GO_TO_BASKET = (By.CSS_SELECTOR, '.btn-group a.btn-default')
    LBL_GOODS_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-6")
    LBL_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
    INPUT_EMAIL_FOR_REGISTRATION = (By.CSS_SELECTOR, "input#id_registration-email")
    INPUT_PASSWORD_FOR_REGISTRATION = (By.CSS_SELECTOR, "input#id_registration-password1")
    REPEAT_PASSWORD_FOR_REGISTRATION = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTER_BTN = (By.NAME, "registration_submit")


