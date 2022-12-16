from base.selenium_base import SeleniumBase
from utils.constants import DepositContractPage as dcp


# Elements at deposit contract page
class DepositContractPage(SeleniumBase):
    # Xpath to web elements in constructor.
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__xpath_next_button = dcp.xpath_next_button
        self.__input_fields_selector = dcp.input_fields_selector
        self.__xpath_change = dcp.xpath_change

    def get_all_input_field(self):
        return self.are_visible('css', self.__input_fields_selector, "Select all input fields")

    def get_next_button(self):
        return self.is_present('xpath', self.__xpath_next_button, "Push on next button")

    def get_fields_present(self):
        return self.is_not_present('css', self.__input_fields_selector, "input fields not present?")
