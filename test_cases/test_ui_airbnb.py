from datetime import datetime, timedelta
import allure
import pytest
from workflows.web_flows import WebFlows
from extensions.verifications import Verifications as Verify


@pytest.mark.usefixtures('init_web_driver')
class TestUI:

    def teardown_method(self):
        WebFlows.refresh_page()

    @allure.title('Test 01: Stays categories')
    @allure.description('This test verifies the appearance of all stays categories')
    def test_stays_categories_appearance(self):
        categories_list = ['Beachfront', 'Rooms', 'Amazing pools', 'OMG!', 'National parks', 'Tiny homes', 'Mansions',
                           'Amazing views', 'Luxe', 'Lakefront', 'Cabins', 'Castles', 'Trending', 'Design',
                           'Countryside', 'Tropical', 'Boats', 'Farms', 'Islands', 'Camping', 'New', 'Ryokans']
        elems = WebFlows.locate_stays_categories(categories_list)
        Verify.verify_elements_displayed(elems)

    @allure.title('Test 02: Auto completion')
    @allure.description('This test verifies auto completion')
    def test_search_auto_complete(self):
        WebFlows.type_in_search_destinations('Tel A')
        result = WebFlows.get_search_suggestions_result_by_index('0')
        Verify.verify_contains(result, 'Tel Aviv-Yafo')

    @allure.title('Test 02.1: Auto completion')
    @allure.description('This demonstrates a failure')
    def test_fail_search_auto_complete(self):
        WebFlows.type_in_search_destinations('Tel A')
        result = WebFlows.get_search_suggestions_result_by_index('0')
        Verify.verify_contains(result, 'Not Tel Aviv-Yafo')

    @allure.title('Test 03: Date picker')
    @allure.description('This test verifies the date picker functionality')
    def test_date_picker(self):
        today = datetime.today().date()
        date_after_week = today + timedelta(days=7)
        today_formatted = today.strftime("%Y-%m-%d")
        date_after_week_formatted = date_after_week.strftime("%Y-%m-%d")
        WebFlows.select_check_in_or_out_date('Check in', today_formatted)
        WebFlows.select_check_in_or_out_date('Check out', date_after_week_formatted)
        check_in = WebFlows.get_selected_date_from('Check in')
        check_out = WebFlows.get_selected_date_from('Check out')
        Verify.verify_equals(check_in, today.strftime('%b %-d'))
        Verify.verify_equals(check_out, date_after_week.strftime('%b %-d'))

    @allure.title('Test 04: Guests picker')
    @allure.description('This test verifies guests picker functionality')
    def test_guests_section(self):
        WebFlows.click_on_who()
        WebFlows.add_guests('adults', 'increase')
        WebFlows.add_guests('pets', 'increase')
        Verify.verify_equals(WebFlows.get_selected_guests_text(), "1 guest, 1 pet")
