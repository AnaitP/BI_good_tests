from .base_page import BasePage
from .locators import UsersPageLocators


class UsersPage(BasePage):

    def add_user(self):
        add_user_button = self.browser.find_element(*UsersPageLocators.ADD_USER_BUTTON)
        add_user_button.click()

