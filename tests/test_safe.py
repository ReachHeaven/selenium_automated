import time
import pytest
from pom.safe_pom import safe_tenancy_page as stp, safe_seepact_page as ssp, safe_nda_page as snp, \
    safe_auth_page as sap, safe_main_page as smp
from utils.constants import UserData as ud

class TestSafe:
    @pytest.mark.usefixtures("safe_contract")
    def test_auth(self):
        auth_page = sap.SafeAuthPage(self.driver)
        auth_page.get_auth_phone().send_keys(ud.phone)
        auth_page.get_auth_password().send_keys(ud.password)
        auth_page.get_auth_button().click()
        auth_page.get_auth_assertation().click()  # for assert

    @pytest.mark.usefixtures("safe_contract")
    def test_seepact(self):
        auth_page = sap.SafeAuthPage(self.driver)
        auth_page.get_auth_phone().send_keys(ud.phone)
        auth_page.get_auth_password().send_keys(ud.password)
        auth_page.get_auth_button().click()
        main_page = smp.SafeMainPage(self.driver)
        main_page.get_seepact().click()
        seepact_page = ssp.SeepactPage(self.driver)
        seepact_page.get_name().send_keys("Hello")
        seepact_page.get_button().click()
        seepact_page.get_assert() # for assert

    @pytest.mark.usefixtures("safe_contract")
    def test_nda(self):
        auth_page = sap.SafeAuthPage(self.driver)
        auth_page.get_auth_phone().send_keys(ud.phone)
        auth_page.get_auth_password().send_keys(ud.password)
        auth_page.get_auth_button().click()
        main_page = smp.SafeMainPage(self.driver)
        main_page.get_nda().click()
        nda_page = snp.NdaPage(self.driver)
        nda_page.get_button().click()
        nda_page.get_assert()  # for assert

    @pytest.mark.usefixtures("safe_contract")
    def test_tenancy(self):
        auth_page = sap.SafeAuthPage(self.driver)
        auth_page.get_auth_phone().send_keys(ud.phone)
        auth_page.get_auth_password().send_keys(ud.password)
        auth_page.get_auth_button().click()
        main_page = smp.SafeMainPage(self.driver)
        main_page.get_teenacy().click()
        tenancy_page = stp.TenancyPage(self.driver)
        time.sleep(2)
        tenancy_page.get_button().click()
        tenancy_page.get_assert().click()     # for assert

    @pytest.mark.usefixtures("safe_contract")
    def test_logout(self):
        auth_page = sap.SafeAuthPage(self.driver)
        auth_page.get_auth_phone().send_keys(ud.phone)
        auth_page.get_auth_password().send_keys(ud.password)
        auth_page.get_auth_button().click()
        auth_page.get_auth_assertation().click()
        auth_page.get_auth_logout().click()
        auth_page.get_logout_assert() # for assert



