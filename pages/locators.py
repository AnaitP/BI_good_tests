from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIC_BUTTON = (By.CSS_SELECTOR, "input.btn")

class MainPageLocators():
    SEQURITY_DROPDOWN = (By.CLASS_NAME, "fa-cogs")
    USER_MENU_ITEM = (By.CLASS_NAME, "fa-user")
    TITLE_INFOM_PANEL = (By.CSS_SELECTOR, "#uncontrolled-tab-example-pane-1 .col-md-8")

class UsersPageLocators():
    ADD_USER_BUTTON = (By.CLASS_NAME, "fa-plus")
    USER_MENU_ITEM = (By.CLASS_NAME, "fa-user")
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    USER_LOGIN = (By.ID, "username")
    ACTIVE = (By.ID, "active")
    EMAIL = (By.ID, "email")
    ROLE = (By.ID, "s2id_autogen1")
    PASSWORD = (By.ID, "password")
    CONFPASSWORD = (By.ID, "conf_password")
    SAVE_BUTTON = (By.CLASS_NAME, "btn-primary")
    ALERT = (By.CSS_SELECTOR,'#alert-container > div')
    FILTER_BUTTON = (By.CLASS_NAME, 'fa-filter')
    EMAIL_FILTER = (By.NAME, 'email')
    EMAIL_FILTER_FIELD = (By.ID, 'email')
    SEARCH_BUTTON = (By.ID, 'search-action')
    EDIT_BUTTON = (By.CLASS_NAME, 'fa-edit')
    USER_LOGIN_FIELD = (By.CSS_SELECTOR,'tbody > tr > td:nth-child(4)')
    SHOW_BUTTON = (By.CSS_SELECTOR, '.btn-default .fa-search')
    RESET_PASSWORD_BUTTON = (By.CSS_SELECTOR, '.btn-primary .fa-lock')

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

