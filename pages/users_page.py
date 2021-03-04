from .base_page import BasePage
from .locators import UsersPageLocators
from selenium.webdriver.common.keys import Keys

first_name_test = 'Тестовый'
last_name_test = 'Тест'
user_login_test = 'Тест'
user_email = 'test@mail.ru'
user_role = 'Alpha'
password_test = '123'
new_login = 'test'
new_password = '321'

class UsersPage(BasePage):

    def add_user(self):
        add_user_button = self.browser.find_element(*UsersPageLocators.ADD_USER_BUTTON)
        add_user_button.click()

    def fill_add_user_fields(self):
        first_name = self.browser.find_element(*UsersPageLocators.FIRST_NAME)
        first_name.send_keys(first_name_test)
        last_name = self.browser.find_element(*UsersPageLocators.LAST_NAME)
        last_name.send_keys(last_name_test)
        user_login = self.browser.find_element(*UsersPageLocators.USER_LOGIN)
        user_login.send_keys(user_login_test)
        active = self.browser.find_element(*UsersPageLocators.ACTIVE)
        active.click()
        email = self.browser.find_element(*UsersPageLocators.EMAIL)
        email.send_keys(user_email)
        role = self.browser.find_element(*UsersPageLocators.ROLE)
        role.click()
        role.send_keys(user_role)
        role.send_keys(Keys.ENTER)
        password = self.browser.find_element(*UsersPageLocators.PASSWORD)
        password.send_keys(password_test)
        conf_password = self.browser.find_element(*UsersPageLocators.CONFPASSWORD)
        conf_password.send_keys(password_test)
        save_button = self.browser.find_element(*UsersPageLocators.SAVE_BUTTON)
        save_button.click()

    def user_should_be_added (self):

        assert self.browser.find_element(*UsersPageLocators.ALERT).text, '×\nДобавлено строк'

    def edit_user_login (self):
        filter_button = self.browser.find_element(*UsersPageLocators.FILTER_BUTTON)
        filter_button.click()
        email_filter = self.browser.find_element(*UsersPageLocators.EMAIL_FILTER)
        email_filter.click()
        email_filter_field = self.browser.find_element(*UsersPageLocators.EMAIL_FILTER_FIELD)
        email_filter_field.send_keys(user_email)
        search_button = self.browser.find_element(*UsersPageLocators.SEARCH_BUTTON)
        search_button.click()
        edit_button = self.browser.find_element(*UsersPageLocators.EDIT_BUTTON)
        edit_button.click()
        user_login = self.browser.find_element(*UsersPageLocators.USER_LOGIN)
        user_login.clear()
        user_login.send_keys(new_login)
        save_button = self.browser.find_element(*UsersPageLocators.SAVE_BUTTON)
        save_button.click()

    def user_login_should_be_edited(self):
        assertion_alert = self.browser.find_element(*UsersPageLocators.ALERT).text
        assertion_login = self.browser.find_element(*UsersPageLocators.USER_LOGIN_FIELD).text
        assert assertion_alert == '×\nСтроки успешно отредактированы'
        assert assertion_login == new_login

    def edit_user_password(self):
        edit_button = self.browser.find_element(*UsersPageLocators.SHOW_BUTTON)
        edit_button.click()
        reset_password = self.browser.find_element(*UsersPageLocators.RESET_PASSWORD_BUTTON)
        reset_password.click()
        password = self.browser.find_element(*UsersPageLocators.PASSWORD)
        password.send_keys(new_password)
        conf_password = self.browser.find_element(*UsersPageLocators.CONFPASSWORD)
        conf_password.send_keys(new_password)
        save_button = self.browser.find_element(*UsersPageLocators.SAVE_BUTTON)
        save_button.click()

    def user_password_should_be_edited(self):
        alert_assertion = self.browser.find_element(*UsersPageLocators.ALERT).text
        assert alert_assertion == '×\nПароль изменен'

