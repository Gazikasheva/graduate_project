from selenium.webdriver.common.by import By

class BasePageLocators ():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

#class MainPageLocators():
    

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