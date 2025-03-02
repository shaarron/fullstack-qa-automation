from selenium.webdriver.common.by import By

dynamic=(By.XPATH,'//span[text()="category_name"]')

class StaysCategories:
    def __init__(self, driver):
        self.driver = driver

    def get_dynamic_catgory(self, categeory_name):
        return self.driver.find_element(dynamic[0], dynamic[1].replace("category_name", categeory_name))
