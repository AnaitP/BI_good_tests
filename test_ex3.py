from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class TestDirectedHierAndDD():  # Проверяем иерархию из шапки и значений таблицы и таблицы среза

    def wait_by_css(self, element_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_locator)))
        return self

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://ss.dev.bnvt.ru/')
        self.driver.find_element_by_css_selector("#username").send_keys("netrika")
        self.driver.find_element_by_css_selector("#password").send_keys("netrika")
        self.driver.find_element_by_css_selector("input.btn").click()
        self.driver.get('http://ss.dev.bnvt.ru/superset/dashboard/179')



    def test_hierDirected1(self):
        # 0+ в графе
        time.sleep(4)  # оставил специально, чтобы граф "пробесился"
        actions = webdriver.ActionChains(self.driver)
        self.wait_by_css('#slice-container-740 > svg > g:nth-child(4) > circle')
        clickPoint = self.driver.find_element_by_css_selector('#slice-container-740 > svg > g:nth-child(4) > circle')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(2)').click()  # клик по меню
        time.sleep(0.5)
        self.wait_by_css('#slice-container-740 > svg > g:nth-child(4) > circle')
        result = self.driver.find_element_by_css_selector('#slice-container-740 > svg > g:nth-child(5) > text').text
        print(result)
        assert result == '2', 'Упало при переходе из hierDirected1'  # проверка появившегося поля


def teardown_method(self):
    self.driver.quit()
