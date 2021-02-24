import pytest
from selenium.webdriver.common.keys import Keys


user_name = 'Тестовый'
family_name = 'Тест'
user_login = 'Тест'
user_email = 'test@mail.ru'
user_role = 'Alpha'
password = '123'
new_login = 'test'
new_password = '321'


class TestUserList:

    def test_create_new_user(self, browser, login):
        browser.get("http://r78-rc-superset.zdrav.netrika.ru/users/list/")
        browser.find_element_by_css_selector('div.panel-body.list-container > span > a > i').click()
        browser.find_element_by_css_selector('#first_name').send_keys(user_name)
        browser.find_element_by_css_selector('#last_name').send_keys(family_name)
        browser.find_element_by_css_selector('#username').send_keys(user_login)
        browser.find_element_by_css_selector('#active').click()
        browser.find_element_by_css_selector('#email').send_keys(user_email)
        browser.find_element_by_css_selector('#s2id_autogen1').click()
        browser.find_element_by_css_selector('#s2id_autogen1').send_keys(user_role)
        browser.find_element_by_css_selector('#s2id_autogen1').send_keys(Keys.ENTER)
        browser.find_element_by_css_selector('#password').send_keys(password)
        browser.find_element_by_css_selector('#conf_password').send_keys(password)
        browser.find_element_by_css_selector('#model_form > div.well.well-sm > button').click()
        assertion = browser.find_element_by_css_selector('#alert-container > div').text
        assert assertion == '×\nДобавлено строк'

    def test_edit_new_user(self, browser):
        browser.find_element_by_css_selector('#filter_form > button').click()
        browser.find_element_by_css_selector('#filter_form > ul > li:nth-child(8) > a').click()
        browser.find_element_by_css_selector('#email').send_keys(user_email)
        browser.find_element_by_css_selector('#search-action').click()
        browser.find_element_by_css_selector('td:nth-child(1) > center > div > a:nth-child(2) > i').click()
        browser.find_element_by_css_selector('#username').clear()
        browser.find_element_by_css_selector('#username').send_keys(new_login)
        browser.find_element_by_css_selector('#model_form > div.well.well-sm > button').click()
        assertion_alert = browser.find_element_by_css_selector('#alert-container > div').text
        assertion_login = browser.find_element_by_css_selector('tbody > tr > td:nth-child(4)').text
        assert assertion_alert == '×\nСтроки успешно отредактированы'
        assert assertion_login == new_login

    def test_change_password(self, browser):
        browser.find_element_by_css_selector('tr > td:nth-child(1) > center > div > a:nth-child(1)').click()
        browser.find_element_by_css_selector('#Home > div.well.well-sm > a.btn.btn-sm.btn-primary').click()
        browser.find_element_by_css_selector('#password').send_keys(new_password)
        browser.find_element_by_css_selector('#conf_password').send_keys(new_password)
        browser.find_element_by_css_selector('#model_form > div.well.well-sm > button').click()
        alert_assertion = browser.find_element_by_css_selector('#alert-container > div').text
        assert alert_assertion == '×\nПароль изменен'

    def test_user_authorization(self, user_browser):
        dashes = user_browser.find_element_by_css_selector('#uncontrolled-tab-example-pane-1 > div '
                                                           '> div > div > div.col-md-8').text
        assert dashes == 'Информационные панели'

    def test_delete_user(self, browser):
        browser.get('http://r78-rc-superset.zdrav.netrika.ru/users/list/?_flt_0_email=test%40mail.ru')
        browser.find_element_by_css_selector('tr > td:nth-child(1) > center > div '
                                             '> a.btn.btn-sm.btn-default.confirm').click()
        browser.find_element_by_css_selector('#modal-confirm-ok').click()
        records = browser.find_element_by_css_selector('body > div.container > div > div.panel.panel-primary '
                                                       '> div.panel-body.list-container > b').text
        alert_assertion = browser.find_element_by_css_selector('#alert-container').text
        assert records == 'Не найдено ни одной записи'
        assert alert_assertion == '×\nУдалено строк'
