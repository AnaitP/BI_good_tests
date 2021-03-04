import pytest
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.users_page import UsersPage



first_name_test = 'Тестовый'
last_name_test = 'Тест'
user_login_test = 'Тест'
user_email = 'test@mail.ru'
user_role = 'Alpha'
password_test = '123'
new_login = 'test'
new_password = '321'


class TestUserList:

    def test_guest_can_go_to_login_page(self, browser, admin_login_fix):

        page = MainPage(browser, browser.current_url)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_users_page()


    def test_admin_can_add_new_user(self, browser):

        page = UsersPage(browser, browser.current_url)
        page.add_user()
        page.fill_add_user_fields()
        page.user_should_be_added()

    def test_admin_can_edit_new_user(self, browser):
        page = UsersPage(browser, browser.current_url)
        page.edit_user_login()
        page.user_login_should_be_edited()

    def test_admin_can_change_password(self, browser):
        page = UsersPage(browser, browser.current_url)
        page.edit_user_password()
        page.user_password_should_be_edited()

    def test_user_authorization(self, user_window_fix, browser):
 #       page = MainPage(browser, browser.current_url)
  #      page.open()
 #      page.user_should_see_main_page()
        page = MainPage(browser, browser.current_url)
        page.user_should_see_main_page()
        assert True






