import selenium
import pytest
from .pages.login_page import LoginPage




def test_admin_login_fix(browser):
    link = "http://r78-rc-superset.zdrav.netrika.ru/"
    page = LoginPage(browser, link)
    page.admin_login()