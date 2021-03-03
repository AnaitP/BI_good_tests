from .base_page import BasePage
from .locators import UsersPageLocators



class UsersPage(BasePage):

    def can_go_to_user_page(browser):

        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
    def add_user(self):
        add_user_button = self.browser.find_element(*UsersPageLocators.ADD_USER_BUTTON)
        add_user_button.click()

    def user_should_be_added (self, browser):
        assertion = browser.find_element_by_css_selector('#alert-container > div').text
        assert assertion == '×\nДобавлено строк'