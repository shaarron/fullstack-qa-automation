import allure
import pytest
import os
import selenium.webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities.common_ops import get_data, get_time_stamp
from utilities.event_listener import EventListener
from utilities.manage_pages import ManagePages

driver = None
action = None


@pytest.fixture(scope='class')
def init_web_driver(request):
    edriver = get_web_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.maximize_window()
    driver.implicitly_wait(int(get_data('WaitTime')))
    driver.get(get_data('Url'))
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    ManagePages.init_web_pages()
    yield
    driver.quit()


def get_web_driver():
    web_driver = get_data('Browser')

    if web_driver.lower() == 'chrome':
        return get_chrome()
    elif web_driver.lower() == 'firefox':
        return get_firefox()
    elif web_driver.lower() == 'edge':
        return get_edge()
    else:
        raise Exception('Input exception, Unrecognized Browser')


def get_chrome():
    srv = Service(ChromeDriverManager().install())
    chrome_driver = selenium.webdriver.Chrome(service=srv)
    return chrome_driver


def get_firefox():
    srv = Service(executable_path=GeckoDriverManager().install())
    firefox_driver = selenium.webdriver.Firefox(service=srv)
    return firefox_driver


def get_edge():
    srv = Service(EdgeChromiumDriverManager().install())
    edge_driver = selenium.webdriver.Edge(service=srv)
    return edge_driver


def pytest_exception_interact(node, call, report):
    if report.failed:
        driver = globals().get('driver', None)
        if driver is not None:
            try:
                screenshot_dir = get_data('ScreenshotPath')
                os.makedirs(screenshot_dir, exist_ok=True)
                image_path = os.path.join(screenshot_dir, f"screen_{get_time_stamp()}.png")
                driver.get_screenshot_as_file(image_path)
                allure.attach.file(image_path, attachment_type=allure.attachment_type.PNG)
                print(f"Screenshot saved: {image_path}")

            except Exception as e:
                print(f"Failed to capture screenshot: {e}")
