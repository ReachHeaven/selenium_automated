from base.selenium_base import SeleniumBase
from utils.constants import SearchContractsPage as scp


class SearchContractsPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__enum_contracts_class = scp.enum_contracts_class
        self.__enum_page_class = scp.enum_page_class

    def get_enum_contracts(self):
        return self.are_present('class_name', self.__enum_contracts_class, "Get num of contracts on header")

    def get_enum_page(self):
        return self.are_present('css', self.__enum_page_class, "Get num of contracts on all page")

