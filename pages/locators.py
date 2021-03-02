from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIC_BUTTON = (By.CSS_SELECTOR, "input.btn")

class MainPageLocators():
    SEQURITY_DROPDOWN = (By.CLASS_NAME, "fa-cogs")
    USER_MENU_ITEM = (By.CLASS_NAME, "fa-user")

class UsersPageLocators():
    ADD_USER_BUTTON = (By.CLASS_NAME, "fa-plus")
    USER_MENU_ITEM = (By.CLASS_NAME, "fa-user")

class AddUserPageLocators():
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    USER_LOGIN = (By.ID, "username")
    ACTIVE = (By.ID, "active")
    EMAIL = (By.ID, "email")
    ROLE = (By.ID, "s2id_autogen1")
    PASSWORD = (By.ID, "password")
    CONFPASSWORD = (By.ID, "conf_password")
    SAVE_BUTTON = (By.CLASS_NAME, "btn-primary")

