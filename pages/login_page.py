from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
from.main_page import MainPage
from.locators import RegisterPageLocators
from.locators import BasePageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL doesn't contain 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
    
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user (self):
        self.should_be_login_page ()
        login=f'{BasePage.generate_random_string(7)}@fakemail.com'
        self.should_fill_registration_form (login, 'GSKY133jft')
    
    def should_fill_registration_form(self,email, password):
        self.should_be_register_form ()
        self.browser.find_element(*RegisterPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*RegisterPageLocators.REG_PASS).send_keys (password)
        self.browser.find_element(*RegisterPageLocators.REG_PASS_CONFIRM).send_keys (password)
        self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        assert self.is_element_present (*RegisterPageLocators.SUCCESS_REGISTRATION), "Something went wrong, registration confirmation is not visible"

    