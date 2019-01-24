import page
from base.base_action import BaseAction


class SearchPage(BaseAction):

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    # 点击搜索按钮
    def click_search(self):
        self.click_element(page.search)

    def send_number(self, content):
        self.send_element(page.search_src_text, content)

    def click_back(self):
        self.click_element(page.imageButton)