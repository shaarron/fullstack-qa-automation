import test_cases.conftest as conf
from page_objects.web_objects.main_search_page import MainSearchPage
from page_objects.web_objects.stays_categories import StaysCategories

web_main_page = None
web_stays_categories = None
class ManagePages:
    @staticmethod
    def init_web_pages():
        globals()['web_main_page'] = MainSearchPage(conf.driver)
        globals()['web_stays_categories'] = StaysCategories(conf.driver)



