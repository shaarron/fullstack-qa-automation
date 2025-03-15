import allure
from selenium.webdriver.remote.webelement import WebElement


class Verifications:
    @staticmethod
    @allure.step('verify equals')
    def verify_equals(actual, expected):
        assert actual == expected, 'Verify Equals Failed, actual: ' + str(
            actual) + ' is not Equals to Expected: ' + str(expected)

    @staticmethod
    @allure.step('verify contains')
    def verify_contains(actual, expected):
        assert expected in actual, 'Verify Contains Failed, actual: ' + str(
            actual) + ' is not contains the expected: ' + str(expected)

    @staticmethod
    @allure.step('verify element is displayed')
    def verify_element_displayed(elem: WebElement):
        assert elem.is_displayed(), f'Verify Is Displayed Failed, element: {elem.text} is not displayed'

    @staticmethod
    @allure.step('verify elements are displayed')
    def verify_elements_displayed(elems):
        failed_elems = []
        for elem in elems:
            if not elem.is_displayed():
                failed_elems.append(elem.text)
        if len(failed_elems) > 0:
            raise AssertionError(f"Verify is display failed for elements {str(failed_elems)}")
