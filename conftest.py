import selenium
import pytest

password = '123'
new_login = 'test'

@pytest.fixture
def setup_class():
    browser.get('http://ss.dev.bnvt.ru/')
    browser.maximize_window()
    browser.find_element_by_css_selector("#username").send_keys("netrika")
    browser.find_element_by_css_selector("#password").send_keys("netrika")
    browser.find_element_by_css_selector("input.btn").click()
    browser.get('http://ss.dev.bnvt.ru/superset/dashboard/179')

@pytest.fixture(scope='session')
def browser():
    browser = selenium.webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.fixture
def login(browser):
    browser.get("http://r78-rc-superset.zdrav.netrika.ru/")
    browser.maximize_window()
    browser.find_element_by_css_selector("#username").send_keys("admin")
    browser.find_element_by_css_selector("#password").send_keys("lifeisgood")
    browser.find_element_by_css_selector("input.btn").click()

@pytest.fixture
def user_browser():
    user_browser = selenium.webdriver.Chrome()
    user_browser.get("http://r78-rc-superset.zdrav.netrika.ru/")
    user_browser.maximize_window()
    user_browser.find_element_by_css_selector("#username").send_keys('test')
    user_browser.find_element_by_css_selector("#password").send_keys('321')
    user_browser.find_element_by_css_selector("input.btn").click()
    yield user_browser
    user_browser.quit()
