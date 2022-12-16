from base.selenium_base import SeleniumBase
from utils.constants import SafeTenancyPage as stp


class TenancyPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__accept = stp.accept
        self.__assert = stp.assertion

    def get_button(self):
        return self.is_present("xpath", self.__accept, "Click on accept button")

    def get_assert(self):
        return self.is_visible("xpath", self.__assert, "Get assert")
