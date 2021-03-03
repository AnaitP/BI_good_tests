from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def admin_login(self):
        login_field = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        login_field.send_keys("admin")
        password_field.send_keys("lifeisgood")
        login_button = self.browser.find_element(*LoginPageLocators.LOGIC_BUTTON)
        login_button.click()

    def user_login(self):

        login_field = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        login_field.send_keys("test")
        password_field.send_keys("321")
        login_button = self.browser.find_element(*LoginPageLocators.LOGIC_BUTTON)
        login_button.click()


