from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    def go_to_users_page(self):
        security_dropdown = self.browser.find_element(*MainPageLocators.SEQURITY_DROPDOWN)
        security_dropdown.click()
        user_menu_item = self.browser.find_element(*MainPageLocators.USER_MENU_ITEM)
        user_menu_item.click()

