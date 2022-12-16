from base.selenium_base import SeleniumBase
from utils.constants import SafeSeepactPage as ssp

class SeepactPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__get_name = ssp.get_name
        self.__button = ssp.button
        self.__assert = ssp.assertion

    def get_name(self):
        return self.is_visible("xpath", self.__get_name, "Name input box")

    def get_button(self):
        return self.is_visible("xpath", self.__button, "Get seepact button")

    def get_assert(self):
        return self.is_visible("xpath", self.__assert, "Get seepact button")
