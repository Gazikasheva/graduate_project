from selenium.webdriver.common.by import By

class BasePageLocators ():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    BASKET_BUTTON= (By.LINK_TEXT, "View basket")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR,'.btn.btn-primary.btn-block')  

class LoginPageLocators ():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators ():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR,".btn-add-to-basket")
    ACTIVE_ITEM = (By.CSS_SELECTOR, ".item.active")
    ADDING_CONFIRMATION = (By.XPATH, '//p[contains(text(), "Your basket total is now")]')
    BASKET_TOTAL = (By.XPATH, '//div/strong [contains(text(), "Basket total")]')
    PRODUCT_NAME = (By.TAG_NAME, 'h1')
    ADDED_PRODUCT_NAME = (By.XPATH, "//div[@id='messages']/div[@class='alert alert-safe alert-noicon alert-success  fade in'][1]//strong") 
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[@class='alert alert-safe alert-noicon alert-success  fade in'][1]")

class BasketPageLocators ():
    BASKET_NAME = (By.TAG_NAME, 'h1')
    BASKET_MESSAGE = (By.CSS_SELECTOR,'#content_inner p')
    BASKET_ITEMS = (By.CSS_SELECTOR,'.basket-items')

class RegisterPageLocators ():
    REG_EMAIL= (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASS = (By.NAME,'registration-password1')
    REG_PASS_CONFIRM = (By.NAME,'registration-password2')
    REGISTER_BUTTON = (By.NAME,'registration_submit')
    SUCCESS_REGISTRATION = (By.CSS_SELECTOR, '.icon-ok-sign')