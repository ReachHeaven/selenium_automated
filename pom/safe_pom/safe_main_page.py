from base.selenium_base import SeleniumBase
from utils.constants import SafeMainPage as smp


class SafeMainPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__seepact_path = smp.seepact_path
        self.__nda_path = smp.nda_path
        self.__teenacy_path = smp.teenacy_path

    def get_seepact(self):
        return self.is_present("xpath", self.__seepact_path, "Get seepact contract")

    def get_nda(self):
        return self.is_present("xpath", self.__nda_path, "Get NDA contract")

    def get_teenacy(self):
        return self.is_present("xpath", self.__teenacy_path, "Get teenacy contract")