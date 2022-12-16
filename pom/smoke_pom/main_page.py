from base.selenium_base import SeleniumBase
from utils.constants import MainPage as mp


# Elements at auth page

class MainPage(SeleniumBase):

    # Xpath to web elements in constructor.
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__xpath_phone = mp.xpath_phone
        self.__xpath_password = mp.xpath_password
        self.__xpath_next = mp.xpath_next
        self.__xpath_first = mp.xpath_first
        self.__xpath_civil = mp.xpath_civil
        self.__xpath_payday = mp.xpath_payday
        self.__xpath_my_templates = mp.xpath_my_templates
        self.__xpath_labor = mp.xpath_labor
        self.__xpath_search = mp.xpath_search
        self.__xpath_new_pass = mp.xpath_new_pass
        self.__xpath_deposit_contract = mp.xpath_deposit_contract
        self.__account_context = mp.account_context
        self.__xpath_logout = mp.xpath_logout
        self.__feedback_name = mp.feedback_name
        self.__feedback_phone = mp.feedback_phone
        self.__feedback_selectors = mp.feedback_selectors
        self.__feedback_button = mp.feedback_button
        self.__xpath_svg = mp.xpath_svg
        self.__xpath_auth_button = mp.xpath_svg

    def get_auth_button(self):
        return self.is_present('xpath', self.__xpath_auth_button, "On auth button")

    def get_feedback_selectors(self):
        return self.are_present('css', self.__feedback_selectors, "On feedback inputs")

    def get_labor_contract(self):
        return self.is_visible('xpath', self.__xpath_labor, "On labor contract")

    def search_present(self):
        return self.is_not_present('xpath', self.__xpath_search, "On labor contract")

    def get_account_context(self):
        return self.is_present('css', self.__account_context, "On account context")

    def get_logout_button(self):
        return self.is_visible('xpath', self.__xpath_logout, "On logout button")

    def get_new_password(self):
        return self.is_present('xpath', self.__xpath_new_pass, "On new pass")

    def get_search_contracts(self):
        return self.is_present('xpath', self.__xpath_search, "On my contracts")

    def get_login_textbox(self):
        return self.is_visible('xpath', self.__xpath_phone, "On login textbox")

    def get_login_password(self):
        return self.is_visible('xpath', self.__xpath_password, "On password textbox")

    def get_logon_button(self):
        return self.is_visible('xpath', self.__xpath_next, "On logon button")

    def get_feedback_name(self):
        return self.is_visible('xpath', self.__feedback_name, "Get feedback name input")

    def get_feedback_phone(self):
        return self.is_present('xpath', self.__feedback_phone, "Get feedback phone input")

    def get_feedback_button(self):
        return self.is_present('xpath', self.__feedback_button, "Get feedback button")

    def feedback_field_present(self):
        return self.is_not_present('xpath', self.__feedback_phone, "Get feedback phone input field present")

    def get_deposit_contracts(self):
        return self.is_present('xpath', self.__xpath_deposit_contract, "On deposit contract")

    def get_templates_button(self):
        return self.is_present('xpath', self.__xpath_my_templates, "On templates button")
