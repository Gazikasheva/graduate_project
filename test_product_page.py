from selenium.webdriver.common.by import By
from.pages.product_page import ProductPage
from.pages.base_page import BasePage
link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage (browser,link)
    page.open ()
    page.add_to_basket ()
    
    
