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
        assert expected in actual , 'Verify Contains Failed, actual: ' + str(
            actual) + ' is not contains the expected: ' + str(expected)

    @staticmethod
    @allure.step('verify element is displayed')
    def is_displayed(elem: WebElement):
        assert elem.is_displayed(), f'Verify is Displayed failed, element: {elem.text} is not displayed'

    @staticmethod
    @allure.step('soft verification (assert) of elements using my implementation')
    def soft_displayed(elems):
        failed_elems = []
        for i in range(len(elems)):
            if not elems[i].is_displayed():
                failed_elems.insert(len(failed_elems), elems[i].text)
        if len(failed_elems) > 0:
            for failed_elem in failed_elems:
                print('Soft Displayed Failed, elements which are failed: ' + str(failed_elem))
            raise AssertionError('Soft displayed failed')
