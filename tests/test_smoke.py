import time
import pytest
import re
from pom.smoke_pom.main_page import MainPage
from pom.smoke_pom.deposit_contract_page import DepositContractPage
from pom.smoke_pom.search_contracts_page import SearchContractsPage
from utils.constants import UserData as ud


class TestSmoke:
    @pytest.mark.usefixtures("setup_test_domain")
    def test_auth(self):
        self.driver.delete_all_cookies()
        auth_page = MainPage(self.driver)
        auth_page.get_login_textbox().send_keys(ud.phone)
        auth_page.get_login_password().send_keys(ud.password)
        next_button = auth_page.get_logon_button()
        next_button.click()
        auth_page.get_account_context().click()  # for assert

    @pytest.mark.usefixtures("setup_test_domain")
    def test_contract(self):
        self.driver.delete_all_cookies()
        auth_page = MainPage(self.driver)
        auth_page.get_login_textbox().send_keys(ud.phone)
        auth_page.get_login_password().send_keys(ud.password)
        next_button = auth_page.get_logon_button()
        next_button.click()
        auth_page.get_templates_button().click()
        auth_page.get_deposit_contracts().click()
        deposit_page = DepositContractPage(self.driver)
        fields = deposit_page.get_all_input_field()
        for field in fields:
            field.send_keys("7777777777")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        deposit_page.get_next_button().click()
        deposit_page.get_fields_present()  # for assert

    @pytest.mark.usefixtures("setup_test_domain")
    def test_contracts_enum(self):
        self.driver.delete_all_cookies()
        auth_page = MainPage(self.driver)
        auth_page.get_login_textbox().send_keys(ud.phone)
        auth_page.get_login_password().send_keys(ud.password)
        next_button = auth_page.get_logon_button()
        next_button.click()
        auth_page.get_search_contracts().click()
        search_page = SearchContractsPage(self.driver)
        time.sleep(1.5)
        string = search_page.get_enum_contracts()[0].text
        header_num = re.split(r'\D', string)
        page_num = search_page.get_enum_page()
        index = 0
        for elements in page_num:
            index += 1
        assert int(header_num[0]) == index

    @pytest.mark.usefixtures("setup_test_domain")
    def test_feedback(self):
        self.driver.delete_all_cookies()
        auth_page = MainPage(self.driver)
        auth_page.get_login_textbox().send_keys(ud.phone)
        auth_page.get_login_password().send_keys(ud.password)
        next_button = auth_page.get_logon_button()
        next_button.click()
        auth_page.get_feedback_name().send_keys("Test")
        auth_page.get_feedback_phone().send_keys("1111111111")
        auth_page.get_feedback_button().click()
        auth_page.feedback_field_present()  # for assert

    @pytest.mark.usefixtures("setup_test_domain")
    def test_logout(self):
        self.driver.delete_all_cookies()
        auth_page = MainPage(self.driver)
        auth_page.get_login_textbox().send_keys(ud.phone)
        auth_page.get_login_password().send_keys(ud.password)
        auth_page.get_logon_button().click()
        auth_page.get_account_context().click()
        auth_page.get_logout_button().click()
        auth_page.get_auth_button().click()  # for assert
