from .base_page import BasePage
from .locators import AddUserPageLocators

first_name_test = 'Тестовый'
last_name_test = 'Тест'
user_login = 'Тест'
user_email = 'test@mail.ru'
user_role = 'Alpha'
password = '123'
new_login = 'test'
new_password = '321'

class AddUserPage(BasePage):

    def fill_add_user_fields(self):
        first_name = self.browser.find_element(*AddUserPageLocators.FIRST_NAME)
        first_name.send_keys(first_name_test)
        last_name = self.browser.find_element(*AddUserPageLocators.LAST_NAME)
        last_name.send_keys(last_name_test)



        user_menu_item.click()