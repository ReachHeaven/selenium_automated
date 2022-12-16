from base.selenium_base import SeleniumBase


# Elements at payday page
class PaydayPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__input_selector = "#q-field__native q-placeholder"
        self.__accept_button_xpath = "/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div[3]/button/span[2]/span"

    def get_all_input(self):
        return self.are_visible('css', self.__input_selector, "Get all input forms on payday page")

    def get_accept_button(self):
        return self.is_visible('xpath', self.__accept_button_xpath, "Done payday document")
