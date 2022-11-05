import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as c_opt
from selenium.webdriver.firefox.options import Options as f_opt

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: ru, en, es etc...")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption ('browser_name')
    user_language = request.config.getoption ('language')

    if browser_name == 'chrome':
        print ("\nstart chrome browser for test..")
        options =  c_opt()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)

    elif browser_name == 'firefox':
        print ("\nstart firefox browser for test..")
        fp = f_opt()
        fp.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(options=fp)
  
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    browser.implicitly_wait (5)
    yield browser
    print("\nquit browser..")
    browser.quit()
