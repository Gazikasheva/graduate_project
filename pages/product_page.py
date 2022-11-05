from .base_page import BasePage
#from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import math
import time
from selenium.common.exceptions import NoAlertPresentException 

class ProductPage(BasePage):
    def should_be_Product_page(self):
        self.should_be_promo_url()
        self.should_be_add_to_basket_button()
        self.should_be_active_item()

    def should_be_promo_url(self):
        assert "promo=newYear" in self.browser.current_url, "URL doesn't contain 'promo=newYear'"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON),"'Add to basket' button is not presented"
    
    def should_be_active_item(self):
        assert self.is_element_present(*ProductPageLocators.ACTIVE_ITEM), "Item form is not presented"
    
    def add_to_basket (self):
        addbutton = self.browser.find_element (*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        addbutton.click()
        self.solve_quiz_and_get_code ()
        assert self.is_element_present (*ProductPageLocators.ADDING_CONFIRMATION), "Adding to the basket is not confirmed"
        
        

        
