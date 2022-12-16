from base.selenium_base import SeleniumBase
from utils.constants import SafeAuthPaths as sap

class SafeAuthPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__xpath_phone = sap.phone
        self.__xpath_password = sap.password
        self.__xpath_sign_in = sap.sign_in
        self.__xpath_assertion = sap.assertion
        self.__xpath_logout = sap.logout
        self.__xpath_logout_assert = sap.logout_assert

    def get_auth_phone(self):
        return self.is_present("xpath", self.__xpath_phone, "Get safe auth phone box")

    def get_auth_password(self):
        return self.is_present("xpath", self.__xpath_password, "Get safe auth password box")

    def get_auth_button(self):
        return self.is_present("xpath", self.__xpath_sign_in, "Get safe auth sign in button")

    def get_auth_assertation(self):
        return self.is_present("xpath", self.__xpath_assertion, "Get safe auth phone header for assertion")

    def get_auth_logout(self):
        return self.is_present("xpath", self.__xpath_logout, "Get logout button")

    def get_logout_assert(self):
        return self.is_visible("xpath", self.__xpath_logout_assert, "Get logout assert")