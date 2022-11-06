from .base_page import BasePage
from .locators import ProductPageLocators


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
        url = self.browser.current_url
        product_name = (self.browser.find_element (*ProductPageLocators.PRODUCT_NAME)).text
        addbutton = self.browser.find_element (*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        addbutton.click()
        self.solve_quiz_and_get_code ()
        self.shoul_be_adding_confirmation()
        self.should_be_added_correct_item (product_name,url)
        self.should_be_still_promo_in_url ()
    
    def shoul_be_adding_confirmation (self):
        assert self.is_element_present (*ProductPageLocators.ADDING_CONFIRMATION), "Adding to the basket is not confirmed"
    
    def should_be_added_correct_item (self,product_name_to_compare_with,initial_url):
        added_element = (self.browser.find_element (*ProductPageLocators.ADDED_PRODUCT_NAME)).text
        assert added_element==product_name_to_compare_with, f"{product_name_to_compare_with} was chosen, but {added_element}was added to basket, an error occured in {initial_url}"
            
    def should_be_still_promo_in_url (self):
        assert "promo=offer" in self.browser.current_url, "basket URL doesn't contain 'promo=offer'"

        
        

        
