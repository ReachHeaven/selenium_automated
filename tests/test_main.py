import pytest

from pom.smoke_pom.main_page import MainPage
from pom.labor_page import LaborPage


# Main test class
@pytest.mark.usefixtures('setup')
class TestMain:
    def test_labor(self):
        self.driver.delete_all_cookies()
        auth_page = MainPage(self.driver)
        auth_page.get_login_textbox().send_keys('7085898115')
        auth_page.get_login_password().send_keys('qweasdzxc')
        next_button = auth_page.get_logon_button()
        next_button.click()
        templates_button = auth_page.get_templates_button()
        templates_button.click()
        to_labor_page = auth_page.get_labor_contract()
        to_labor_page.click()
        labor_page = LaborPage(self.driver)
        labor_page.get_name().send_keys('1')
        labor_page.get_id().send_keys('111111111111')
        labor_page.get_date().send_keys('11111111')
        labor_page.get_iin_or_rep().send_keys('111111111111')
        labor_page.get_address().send_keys('1')
        labor_page.get_address_reg().send_keys('1')
        labor_page.get_phone().send_keys('7478715250')
        labor_page.get_employee().send_keys('QA')
        labor_page.get_end_date().send_keys('99999999')
        labor_page.get_start_date().send_keys('11111111')
        labor_page.get_time_first().send_keys('1111')
        labor_page.get_time_second().send_keys('1111')
        labor_page.get_time_third().send_keys('1111')
        labor_page.get_time_last().send_keys('1111')
        labor_page.get_vacation().send_keys('11')
        labor_page.get_salary().send_keys('11')
        labor_page.get_extra().send_keys('11')
        labor_page.get_first_check().click()
        labor_page.get_second_check().click()
        labor_page.get_button().click()
        assert True

    def test_change_labor(self):
        self.driver.delete_all_cookies()
        auth_page = MainPage(self.driver)
        auth_page.get_login_textbox().send_keys('7478715250')
        auth_page.get_login_password().send_keys('Amirov141197')
        next_button = auth_page.get_logon_button()
        next_button.click()
        templates_button = auth_page.get_templates_button()
        templates_button.click()
        to_labor_page = auth_page.get_labor_contract()
        to_labor_page.click()
        labor_page = LaborPage(self.driver)
        labor_page.get_name().send_keys('1')
        labor_page.get_id().send_keys('111111111111')
        labor_page.get_date().send_keys('11111111')
        labor_page.get_iin_or_rep().send_keys('111111111111')
        labor_page.get_address().send_keys('1')
        labor_page.get_address_reg().send_keys('1')
        labor_page.get_phone().send_keys('7478715250')
        labor_page.get_employee().send_keys('QA')
        labor_page.get_end_date().send_keys('99999999')
        labor_page.get_start_date().send_keys('11111111')
        labor_page.get_time_first().send_keys('1111')
        labor_page.get_time_second().send_keys('1111')
        labor_page.get_time_third().send_keys('1111')
        labor_page.get_time_last().send_keys('1111')
        labor_page.get_vacation().send_keys('11')
        labor_page.get_salary().send_keys('11')
        labor_page.get_extra().send_keys('11')
        labor_page.get_first_check().click()
        labor_page.get_second_check().click()
        labor_page.get_button().click()
        #WebDriverWait(self.driver, 15)
        labor_page.get_change_button().click()
        labor_page.get_name().send_keys('2')
        labor_page.get_id().send_keys('222222222222')
        labor_page.get_date().send_keys('22222222')
        labor_page.get_iin_or_rep().send_keys('222222222222')
        labor_page.get_address().send_keys('2')
        labor_page.get_address_reg().send_keys('2')
        labor_page.get_phone().send_keys('7478715250')
        labor_page.get_employee().send_keys('QQ')
        labor_page.get_end_date().send_keys('22222222')
        labor_page.get_start_date().send_keys('33333333')
        labor_page.get_time_first().send_keys('2222')
        labor_page.get_time_second().send_keys('2222')
        labor_page.get_time_third().send_keys('2222')
        labor_page.get_time_last().send_keys('2222')
        labor_page.get_vacation().send_keys('22')
        labor_page.get_salary().send_keys('22')
        labor_page.get_extra().send_keys('22')
        assert True

    # def test_payday_page(self):
    #     self.driver.delete_all_cookies()
    #     auth_page = AuthPage(self.driver)
    #     auth_page.get_login_textbox().send_keys('7478715250')
    #     auth_page.get_login_password().send_keys('Amirov141197')
    #     next_button = auth_page.get_logon_button()
    #     next_button.click()
    #     WebDriverWait(self.driver, 15)
    #     loam_button = auth_page.get_loam_button()
    #     loam_button.click()
    #     self.driver.execute_script("window.scrollTo(100,document.body.scrollHeight);")
    #     WebDriverWait(self.driver, 20)
    #     payday_button = auth_page.get_payday_button()
    #     payday_button.click()
    #     payday_page = PaydayPage(self.driver)
    #     input_list = payday_page.get_all_input()
    #     for views in input_list:
    #         views.sendkeys("7479999999")
    #     accept = payday_page.get_accept_button()
    #     accept.click()
    #
    # def test_civil_page(self):
    #     auth_page = AuthPage(self.driver)
    #     auth_page.get_login_textbox().send_keys('7478715250')
    #     auth_page.get_login_password().send_keys('Amirov141197')
    #     next_button = auth_page.get_logon_button()
    #     next_button.click()
    #     WebDriverWait(self.driver, 15)
    #     loam_button = auth_page.get_loam_button()
    #     loam_button.click()
    #     civil_button = auth_page.get_civil_button()
    #     civil_button.click()
    #
    #     civil_page = CivilLawPage(self.driver)
    #
    #     id_document = civil_page.get_civil_number()
    #     id_document.send_keys("1")
    #
    #     main = civil_page.get_civil_main()
    #     main.send_keys("1")
    #
    #     paydays = civil_page.get_civil_paydays()
    #     paydays.send_keys("1")
    #
    #     price = civil_page.get_civil_price()
    #     price.send_keys("1")
    #
    #     extra = civil_page.get_civil_extra()
    #     extra.send_keys("1")
    #
    #     company = civil_page.get_civil_company()
    #     company.send_keys("1")
    #
    #     adr = civil_page.get_civil_adr()
    #     adr.send_keys("1")
    #
    #     checkbox = civil_page.get_civil_checkbox()
    #     checkbox.click()
    #
    #     identity = civil_page.get_civil_id()
    #     identity.send_keys("1")
    #
    #     bank = civil_page.get_civil_bank()
    #     bank.send_keys("1")
    #
    #     bik = civil_page.get_civil_bik()
    #     bik.send_keys("1")
    #
    #     iik = civil_page.get_civil_iik()
    #     iik.send_keys("1")
    #
    #     owner = civil_page.get_civil_owner()
    #     owner.send_keys("1")
    #
    #     owner_phone = civil_page.get_civil_owner_phone()
    #     owner_phone.send_keys("7479999999")
    #
    #     employer = civil_page.get_civil_employer()
    #     employer.send_keys("1")
    #
    #     employer_addr = civil_page.get_civil_employer_addr()
    #     employer_addr.send_keys("1")
    #
    #     e_reg = civil_page.get_civil_employer_reg()
    #     e_reg.send_keys("1")
    #
    #     e_id = civil_page.get_civil_employer_id()
    #     e_id.send_keys("1")
    #
    #     e_iin = civil_page.get_civil_employer_iin()
    #     e_iin.send_keys("1")
    #
    #     bank = civil_page.get_civil_bank()
    #     bank.send_keys("1")
    #
    #     bill = civil_page.get_civil_bill()
    #     bill.send_keys("1")
    #
    #     e_phone = civil_page.get_civil_employer_phone()
    #     e_phone.send_keys("7479999999")
    #
    #     button = civil_page.get_accept_button()
    #     button.click()
