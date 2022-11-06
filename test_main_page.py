from.pages.main_page import MainPage
from .pages.login_page import LoginPage
from.pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self,browser):
        page = MainPage (browser,link)
        page.open ()
        page.go_to_login_page ()
        login_page = LoginPage (browser,browser.current_url)  # type: ignore
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self,browser):
        page = MainPage (browser, link)
        page.open ()
        page.should_be_login_link ()

def test_guest_cant_see_product_in_basket_opened_from_main_page (browser):
    page = BasketPage (browser,link)
    page.open ()
    page.should_be_basket_enterable()
    page.should_basket_be_empty_by_default ()


@pytest.mark.new
def test_guest_can_register (browser):
    page = MainPage (browser,link)
    page.open ()
    page.go_to_login_page ()
    login_page = LoginPage (browser,browser.current_url)  # type: ignore
    LoginPage.register_new_user (login_page)

