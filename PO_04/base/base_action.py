import time


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, tuple_param):
        time.sleep(1)
        return self.driver.find_element(tuple_param[0], tuple_param[1])

    def find_elements(self, tuple_param):
        time.sleep(1)
        return self.driver.find_elements(tuple_param[0], tuple_param[1])

    def click_element(self, tuple_param):
        self.find_element(tuple_param).click()

    def send_element(self, tuple_param, content):
        input = self.find_element(tuple_param)
        input.clear()
        input.send_keys(content)
