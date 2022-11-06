from selenium.webdriver.common.by import By
from.pages.product_page import ProductPage
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"

@pytest.mark.parametrize ("offer", [1,2,3,4,5,6, 
                            pytest.param(7, marks=pytest.mark.xfail),
                                8,9])
def test_guest_can_add_product_to_basket(browser,offer):
    url = f'{link}{offer}'
    page = ProductPage (browser,url)
    page.open ()
    page.add_to_basket ()
    
    

    
