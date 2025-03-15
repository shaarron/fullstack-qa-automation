import allure
from extensions.ui_actions import UiActions
import utilities.manage_pages as page
from page_objects.web_objects.main_search_page import search_input
from utilities.common_ops import wait, For
from test_cases import conftest


class WebFlows:

    @staticmethod
    @allure.step('click on search to expand it')
    def expand_big_search():
        UiActions.click(page.web_main_page.get_minimized_search_icon())

    @staticmethod
    @allure.step('check if minimized search')
    def get_minimized_search_element():
        return page.web_main_page.get_minimized_search_icon()

    @staticmethod
    @allure.step("select 'search destinations'")
    def click_on_search_destinations():
        UiActions.click(page.web_main_page.get_search_button())

    @staticmethod
    @allure.step("type in text in search destination")
    def type_in_search_destinations(text):
        wait(For.ELEMENT_DISPLAYED, search_input)
        UiActions.update_text(page.web_main_page.get_search_button(), text)

    @staticmethod
    @allure.step('get available search suggestions by index')
    def get_search_suggestions_result_by_index(index):
        suggestion = page.web_main_page.get_search_suggestions(index=index)

        return suggestion.text

    @staticmethod
    @allure.step('get the available categories names')
    def locate_stays_categories(categories_list):
        located_elements = []
        for category in categories_list:
            elem = page.web_stays_categories.get_dynamic_category(category)
            located_elements.append(elem)
        return located_elements

    @staticmethod
    @allure.step('select the date in check in or check out')
    def select_check_in_or_out_date(check_type, date):
        active_tab = page.web_main_page.get_active_tab(tab_text=check_type)
        if active_tab is None:
            if check_type == 'Check in':
                UiActions.click(page.web_main_page.get_check_in())
            elif check_type == 'Check out':
                UiActions.click(page.web_main_page.get_check_out())
        else:
            if check_type == 'Check in' and not active_tab.text == 'Check in':
                UiActions.click(page.web_main_page.get_check_in())
            if check_type == 'Check out' and not active_tab.text == 'Check out':
                UiActions.click(page.web_main_page.get_check_out())
        UiActions.click(page.web_main_page.select_date(date))

    @staticmethod
    @allure.step('get the selected date of check in or check out')
    def get_selected_date_from(check_in_or_out):
        element = page.web_main_page.get_check_in_or_out_selected_date(check_in_or_out)
        return element.text

    @staticmethod
    @allure.step('click on who to select guests')
    def click_on_who():
        UiActions.click(page.web_main_page.get_guests_tab())

    @staticmethod
    @allure.step('refresh - to reset the page')
    def refresh_page():
        UiActions.refresh_page()

    @staticmethod
    @allure.step('add guests')
    def add_guests(who, increase_or_decrease):
        UiActions.click(page.web_main_page.get_guests_stepper(who, increase_or_decrease))

    @staticmethod
    @allure.step('get selected guests')
    def get_selected_guests_text():
        guests = page.web_main_page.get_selected_guests()
        return guests.text

