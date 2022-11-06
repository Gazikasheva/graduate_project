from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators
from .locators import MainPageLocators
import time

class BasketPage (BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def should_be_basket_enterable (self):
        self.should_be_basket_button()
        basket_button = self.browser.find_element (*MainPageLocators.BASKET_BUTTON)
        basket_button.click()
        self.should_be_basket_url ()
        assert self.is_element_present (*BasketPageLocators.BASKET_NAME), 'Basket header is missing'
        
    def should_be_basket_button (self):
        assert self.is_element_present(*MainPageLocators.BASKET_BUTTON), "Basket button is not presented" 
    
    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "URL doesn't contain 'basket'"

    def should_basket_be_empty_by_default (self):
        assert self.is_not_element_present (*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"
        basket_empty_message = self.browser.find_element (*BasketPageLocators.BASKET_MESSAGE)
        assert "empty" in basket_empty_message.text,f"'Your basket is empty' instead of {basket_empty_message} is expected"
