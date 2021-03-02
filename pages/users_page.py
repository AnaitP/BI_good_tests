from .base_page import BasePage
from .locators import UsersPageLocators


class UsersPage(BasePage):

    def add_user(self):
        add_user_button = self.browser.find_element(*UsersPageLocators.ADD_USER_BUTTON)
        add_user_button.click()

    def user_should_be_added (self)
        assertion = browser.find_element_by_css_selector('#alert-container > div').text
        assert assertion == '×\nДобавлено строк'