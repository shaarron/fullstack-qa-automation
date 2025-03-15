from selenium.webdriver.common.by import By


class StaysCategories:
    def __init__(self, driver):
        self.driver = driver

    def get_dynamic_category(self, category_name):
        dynamic = (By.XPATH, f'//span[text()="{category_name}"]')
        return self.driver.find_element(*dynamic)
