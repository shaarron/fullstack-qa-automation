from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

select_date = (By.XPATH, "//button[@data-state--date-string='placeholder']")
selected_check_in_or_out_date = (By.XPATH, "//div[contains(text(), 'Check in/out')]/following-sibling::div")
check_out_tab = (By.XPATH, "//*[text()='Check out']")
guests_tab = (By.XPATH, "//*[text()='Who']")
search_input = (By.XPATH, "//input[@data-testid='structured-search-input-field-query']")
minimized_search = (By.XPATH, "//div[@data-testid='little-search-icon']")
close_opening_video = (By.CLASS_NAME, "i9dqh6z")
guests_stepper_button = (By.XPATH, "//button[@data-testid='stepper-who-increase-button']")
selected_guests = (By.XPATH, "//div[text()='Who']/following-sibling::div[1]")
check_in_tab = (By.XPATH, "//*[text()='Check in']")


class MainSearchPage:
    def __init__(self, driver):
        self.driver = driver

    def select_date(self, date):
        return self.driver.find_element(select_date[0], select_date[1].replace('placeholder', date))

    def get_check_in(self):
        return self.driver.find_element(check_in_tab[0], check_in_tab[1])

    def get_check_in_or_out_selected_date(self, option):
        capitalized_option = option.capitalize()
        return self.driver.find_element(selected_check_in_or_out_date[0],
                                        selected_check_in_or_out_date[1].replace('Check in/out', capitalized_option))

    def get_check_out(self):
        return self.driver.find_element(check_out_tab[0], check_out_tab[1])

    # todo: consider changing all parameters to tuple unpacking
    def get_active_tab(self, tab_text):
        dynamic_active_tab = (By.XPATH, f"//div[@aria-expanded='true']//div[text()='{tab_text}']")
        try:
            return self.driver.find_element(*dynamic_active_tab)
        except NoSuchElementException:
            return None

    def get_guests_tab(self):
        return self.driver.find_element(guests_tab[0], guests_tab[1])

    def get_search_button(self):
        return self.driver.find_element(search_input[0], search_input[1])

    def get_minimized_search_icon(self):
        return self.driver.find_element(minimized_search[0], minimized_search[1])

    def get_search_suggestions(self, index):
        search_suggestions = (By.ID, "bigsearch-query-location-suggestion-X")
        return self.driver.find_element(search_suggestions[0], search_suggestions[1].replace('X', index))

    def get_guests_stepper(self, who, decrease_or_increase):
        return self.driver.find_element(guests_stepper_button[0],
                                        guests_stepper_button[1].replace('who', who).replace('increase',
                                                                                             decrease_or_increase))

    def get_selected_guests(self):
        return self.driver.find_element(selected_guests[0], selected_guests[1])
