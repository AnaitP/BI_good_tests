from .base_page import BasePage
from .locators import AddUserPageLocators
from selenium.webdriver.common.keys import Keys

first_name_test = 'Тестовый'
last_name_test = 'Тест'
user_login_test = 'Тест'
user_email = 'test@mail.ru'
user_role = 'Alpha'
password_test = '123'
new_login = 'test'
new_password = '321'

class AddUserPage(BasePage):

    def fill_add_user_fields(self):
        first_name = self.browser.find_element(*AddUserPageLocators.FIRST_NAME)
        first_name.send_keys(first_name_test)
        last_name = self.browser.find_element(*AddUserPageLocators.LAST_NAME)
        last_name.send_keys(last_name_test)
        user_login = self.browser.find_element(*AddUserPageLocators.USER_LOGIN)
        user_login.send_keys(user_login)
        active = self.browser.find_element(*AddUserPageLocators.ACTIVE)
        active.click()
        email = self.browser.find_element(*AddUserPageLocators.EMAIL)
        email.send_keys(user_email)
        role = self.browser.find_element(*AddUserPageLocators.ROLE)
        role.click()
        role.send_keys(user_role)
        role.send_keys(Keys.ENTER)
        password = self.browser.find_element(*AddUserPageLocators.PASSWORD)
        password.send_keys(password_test)
        conf_password = self.browser.find_element(*AddUserPageLocators.CONFPASSWORD)
        conf_password.send_keys(password_test)
        save_button = self.browser.find_element(*AddUserPageLocators.SAVE_BUTTON)
        save_button.click()

