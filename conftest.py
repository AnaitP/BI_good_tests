import selenium
import pytest
from .pages.login_page import LoginPage
from .pages.main_page import MainPage

password = '123'
new_login = 'test'

@pytest.fixture
def setup_class():
    browser.get('http://ss.dev.bnvt.ru/')

    browser.find_element_by_css_selector("#username").send_keys("netrika")
    browser.find_element_by_css_selector("#password").send_keys("netrika")
    browser.find_element_by_css_selector("input.btn").click()
    browser.get('http://ss.dev.bnvt.ru/superset/dashboard/179')

@pytest.fixture(scope='session')
def browser():
    browser = selenium.webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture
def admin_login_fix(browser):
    link = "http://r78-rc-superset.zdrav.netrika.ru/"
    page = LoginPage(browser, link)
    page.open()
    page.admin_login()


@pytest.fixture(scope='function')
def user_window_fix(browser):
    browser = selenium.webdriver.Chrome()
    link = "http://r78-rc-superset.zdrav.netrika.ru/"
    page = LoginPage(browser, link)
    page.open()
    page.user_login()
    yield page
    page.browser.quit()
