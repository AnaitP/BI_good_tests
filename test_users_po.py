import pytest
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.users_page import UsersPage
from .pages.add_user_page import AddUserPage


user_name = 'Тестовый'
family_name = 'Тест'
user_login = 'Тест'
user_email = 'test@mail.ru'
user_role = 'Alpha'
password = '123'
new_login = 'test'
new_password = '321'


class TestUserList:

    def test_guest_can_go_to_login_page(self, browser, admin_login_fix):

       page = MainPage(browser)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
      # page.open()  # открываем страницу
       page.go_to_users_page()


   # def admin_can_add_new_user(self, browser, admin_login_fix):





