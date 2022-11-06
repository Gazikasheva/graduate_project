from selenium.webdriver.common.by import By
from.pages.product_page import ProductPage
from.pages.main_page import MainPage
from.pages.basket_page import BasketPage

import pytest
import time

promo_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
link ='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page  (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page ()
    

@pytest.mark.parametrize ("offer", [1])#,2,3,4,5,6, 
                            #pytest.param(7, marks=pytest.mark.xfail),
                                #8,9])
def test_guest_can_add_product_to_basket(browser,offer):
    url = f'{promo_link}{offer}'
    page = ProductPage (browser,url)
    page.open ()
    page.add_to_basket_promo ()
    

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    page = ProductPage (browser,link)
    page.open ()
    page.add_to_basket ()
    page.should_not_be_success_message ()

def test_guest_cant_see_success_message (browser):
    page = ProductPage (browser,link)
    page.open ()
    page.should_not_be_success_message ()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket (browser): 
    page = ProductPage (browser,link)
    page.open ()
    page.add_to_basket ()
    page.should_some_element_disappeared ()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
        page = BasketPage (browser,link)
        page.open ()
        page.should_be_basket_enterable()
        page.should_basket_be_empty_by_default ()

#Гость открывает страницу товара
#Переходит в корзину по кнопке в шапке 
#Ожидаем, что в корзине нет товаров
#Ожидаем, что есть текст о том что корзина пуста 