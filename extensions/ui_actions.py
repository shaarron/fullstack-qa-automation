import allure
from selenium.webdriver.remote.webelement import WebElement

from test_cases import conftest


class UiActions:

    @staticmethod
    @allure.step('click on element')
    def click(elem: WebElement):
        elem.click()

    @staticmethod
    @allure.step('updating text')
    def update_text(elem: WebElement, value: str):
        elem.send_keys(value)

    @staticmethod
    @allure.step('refresh page')
    def refresh_page():
        conftest.driver.refresh()
