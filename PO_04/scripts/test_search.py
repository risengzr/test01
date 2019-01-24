import os,sys
sys.path.append(os.getcwd())
from base.read_yaml import read_data
from page.search_page import SearchPage
from base.driver import init_driver
import page
import time
import pytest


def read_yaml_file():
    return read_data("search.yaml").get("search")

class TestSearch:

    def setup_class(self):
        self.driver = init_driver(page.appPackage, page.appActivity)
        self.search_page = SearchPage(self.driver)

    @pytest.mark.parametrize("input_number", read_yaml_file())
    def test_search(self, input_number):
        self.search_page.click_search()
        self.search_page.send_number(input_number)
        self.search_page.click_back()

    def teardown_class(self):
        time.sleep(3)
        self.driver.quit()
