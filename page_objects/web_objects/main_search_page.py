from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

check_out_tab = (By.XPATH, "//*[text()='Check out']")
guests_tab = (By.XPATH, "//*[text()='Who']")
search_input = (By.XPATH, "//input[@data-testid='structured-search-input-field-query']")
minimized_search = (By.XPATH, "//div[@data-testid='little-search-icon']")
close_opening_video = (By.CLASS_NAME, "i9dqh6z")
selected_guests = (By.XPATH, "//div[text()='Who']/following-sibling::div[1]")
check_in_tab = (By.XPATH, "//*[text()='Check in']")


class MainSearchPage:
    def __init__(self, driver):
        self.driver = driver

    def select_date(self, date):
        select_date = (By.XPATH, f"//button[@data-state--date-string='{date}']")
        return self.driver.find_element(*select_date)

    def get_check_in(self):
        return self.driver.find_element(check_in_tab[0], check_in_tab[1])

    def get_check_in_or_out_selected_date(self, option):
        capitalized_option = option.capitalize()
        selected_check_in_or_out_date = (By.XPATH, f"//div[contains(text(), '{capitalized_option}')]/following-sibling::div")
        return self.driver.find_element(*selected_check_in_or_out_date)

    def get_check_out(self):
        return self.driver.find_element(*check_out_tab)

    def get_active_tab(self, tab_text):
        dynamic_active_tab = (By.XPATH, f"//div[@aria-expanded='true']//div[text()='{tab_text}']")
        try:
            return self.driver.find_element(*dynamic_active_tab)
        except NoSuchElementException:
            return None

    def get_guests_tab(self):
        return self.driver.find_element(*guests_tab)

    def get_search_button(self):
        return self.driver.find_element(*search_input)

    def get_minimized_search_icon(self):
        return self.driver.find_element(*minimized_search)

    def get_search_suggestions(self, index):
        search_suggestions = (By.ID, f"bigsearch-query-location-suggestion-{index}")
        return self.driver.find_element(*search_suggestions)

    def get_guests_stepper(self, who, decrease_or_increase):
        guests_stepper_button = (By.XPATH, f"//button[@data-testid='stepper-{who}-{decrease_or_increase}-button']")
        return self.driver.find_element(*guests_stepper_button)

    def get_selected_guests(self):
        return self.driver.find_element(*selected_guests)
