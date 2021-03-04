from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.maximize_window()
        self.browser.implicitly_wait(timeout)
        self.user_browser = browser


    def open(self):
        self.browser.get(self.url)

    def quit(self):
        self.browser.quit(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True