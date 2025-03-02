import allure
from selenium.webdriver.remote.webelement import WebElement

class UiActions:

    @staticmethod
    @allure.step('click on element')
    def click(elem: WebElement):
        elem.click()

    @staticmethod
    @allure.step('updating text')
    def update_text(elem: WebElement, value: str):
        elem.send_keys(value)
