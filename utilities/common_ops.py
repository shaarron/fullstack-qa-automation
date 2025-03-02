import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_cases.conftest as conf
import xml.etree.ElementTree as ET
import os


def get_data(node_name):
    parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(parent_path, "configuration", "data.xml")
    root = ET.parse(file_path).getroot()
    node = root.find('.//' + node_name)
    return node.text


def wait(for_element, elem):
    if for_element == For.ELEMENT_EXISTS:
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.presence_of_element_located((elem[0], elem[1])))
    if for_element == For.ELEMENT_DISPLAYED:
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(
            EC.visibility_of_element_located((elem[0], elem[1])))


class For:
    ELEMENT_EXISTS = 'element_exists'
    ELEMENT_DISPLAYED = 'element_displayed'


def get_time_stamp():
    return time.time()
