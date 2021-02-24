from selenium import webdriver
import pytest
from pytest_testrail.plugin import testrail

import time

@testrail("C16535")
class TestDirectedHierAndDD():  # Проверяем иерархию из шапки и значений таблицы и таблицы среза

    def test_hierDirected1(self, browser):
        # 0+ в графе
        time.sleep(4)  # оставил специально, чтобы граф "пробесился"
        actions = webdriver.ActionChains(browser)

        clickPoint = browser.find_element_by_css_selector('#slice-container-740 > svg > g:nth-child(4) > circle')
        actions.move_to_element(clickPoint).context_click().perform()
        browser.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(2)').click()  # клик по меню
        time.sleep(0.5)
        result = browser.find_element_by_css_selector('#slice-container-740 > svg > g:nth-child(5) > text').text
        print(result)
        assert result == '2', 'Упало при переходе из hierDirected1'  # проверка появившегося поля

    def test_hierDirected2(self, browser):
        # Красногвардейский район в графе
        time.sleep(4)
        actions = webdriver.ActionChains(browser)

        clickPoint = browser.find_element_by_css_selector('#slice-container-740 > svg > g:nth-child(9) > circle')
        actions.move_to_element(clickPoint).context_click().perform()
        button = browser.find_element_by_css_selector('.d3-context-menu > ul:nth-child(1) > li:nth-child(2)')
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()  # клик по меню
        time.sleep(0.5)
        result = browser.find_element_by_css_selector('#slice-container-740 > svg > g:nth-child(13) > text').text
        print(result)
        assert result == 'ДГП №68', 'Упало при переходе из hierDirected2'  # проверка появившегося поля

    def test_ddDirected2(self, browser):
        # Красногвардейский район в графе
        time.sleep(4)  # оставил специально, чтобы граф "пробесился"
        actions = webdriver.ActionChains(browser)

        clickPoint = browser.find_element_by_css_selector('#slice-container-740 > svg > g:nth-child(13) > circle')
        actions.move_to_element(clickPoint).context_click().perform()
        browser.find_element_by_css_selector(
            '.d3-context-menu ul li:nth-of-type(4)').click()  # клик по меню
        time.sleep(0.5)
        result = browser.find_element_by_css_selector('div:nth-of-type(1) > .slice-cell .slice_container.table '
                                                      '> .dataTables_wrapper.dt-bootstrap.form-inline.no-footer .'
                                                      'dataTables_scrollBody > table[role="grid"] > tbody > '
                                                      'tr:nth-of-type(1) > td:nth-of-type(1) > .like-pre').text
        result1 = browser.find_element_by_css_selector('div:nth-of-type(1) > .slice-cell .slice_container.table > '
                                                       '.dataTables_wrapper.dt-bootstrap.form-inline.no-footer '
                                                       '.dataTables_scrollBody > table[role="grid"] > tbody > '
                                                       'tr:nth-of-type(2) > td:nth-of-type(2) > .like-pre').text
        result2 = browser.find_element_by_css_selector('div:nth-of-type(1) > .slice-cell .slice_container.table > '
                                                       '.dataTables_wrapper.dt-bootstrap.form-inline.no-footer '
                                                       '.dataTables_scrollBody > table[role="grid"] > tbody > '
                                                       'tr:nth-of-type(3) > td[title="3"] > .like-pre').text
        print(result)
        assert result == 'Красногвардейский район', 'Упало при переходе из hierDirected1'  # проверка появившегося поля
        assert result1 == 'ДГП №68', 'Упало при переходе из hierDirected1'  # проверка появившегося поля
        assert result2 == '3', 'Упало при переходе из hierDirected1'  # проверка появившегося поля
