from selenium import webdriver
import pytest




@pytest.fixture(scope='class', autouse=True)
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get('http://ss.dev.bnvt.ru/')
    browser.find_element_by_name("username").send_keys("netrika")
    browser.find_element_by_name("password").send_keys("netrika")
    browser.find_element_by_css_selector("input.btn").click()
    browser.get('http://ss.dev.bnvt.ru/superset/dashboard/179')
    yield browser
    browser.quit()

