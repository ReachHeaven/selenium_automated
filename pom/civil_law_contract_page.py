from base.selenium_base import SeleniumBase


# Elements at civil law page

class CivilLawPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__xpath_number = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[2]/div[2]/div[" \
                              "1]/label/div/div/div/input "
        self.__xpath_main = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[2]/div[2]/div[" \
                            "3]/label/div/div/div/input "
        self.__xpath_paydays = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[2]/div[2]/div[" \
                               "5]/label/div/div/div[1]/input "
        self.__xpath_price = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[2]/div[2]/div[" \
                             "6]/label/div/div/div[1]/input "
        self.__xpath_extra = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[2]/div[2]/div[" \
                             "7]/label/div/div/div[1]/input "
        self.__xpath_company = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[3]/div[2]/div[" \
                               "1]/label/div/div/div/input "
        self.__xpath_adr = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[3]/div[2]/div[" \
                           "2]/label/div/div/div/input "
        self.__xpath_checkbox = "//*[@id=\"q-app\"]/div/div/div/div/div[2]/div[2]/form/div[3]/div[2]/div[4]/div"
        self.__xpath_id = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[3]/div[2]/div[" \
                          "5]/label/div/div/div/input "
        self.__xpath_bank_name = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[3]/div[2]/div[" \
                                 "6]/label/div/div/div/input "
        self.__xpath_bik = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[3]/div[2]/div[" \
                           "6]/label/div/div/div/input "
        self.__xpath_iik = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[3]/div[2]/div[" \
                           "8]/label/div/div/div/input "
        self.__xpath_owner = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[3]/div[2]/div[" \
                             "9]/label/div/div/div/input "
        self.__xpath_owner_phone = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[3]/div[2]/div[" \
                                   "10]/label/div/div[1]/div[2]/input "
        self.__xpath_employer = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[4]/div[2]/div[" \
                                "1]/label/div/div/div/input "
        self.__xpath_employer_addr = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[4]/div[2]/div[" \
                                     "2]/label/div/div/div/input "
        self.__xpath_employer_reg = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[4]/div[2]/div[" \
                                    "3]/label/div/div/div/input "
        self.__xpath_employer_id = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[4]/div[2]/div[" \
                                   "5]/label/div/div/div/input "
        self.__xpath_employer_iin = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[4]/div[2]/div[" \
                                    "7]/label/div/div/div/input "
        self.__xpath_employer_bank = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[4]/div[2]/div[" \
                                     "8]/label/div/div/div/input "
        self.__xpath_employer_bill = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[4]/div[2]/div[" \
                                     "9]/label/div/div/div/input "
        self.__xpath_employer_phone = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[4]/div[2]/div[" \
                                      "10]/label/div/div[1]/div[2]/input "
        self.__xpath_accept_button = "/html/body/div[1]/div/div/div/div/div[2]/div[2]/form/div[7]/button/span[2]/span"

    def get_civil_number(self):
        return self.is_visible('xpath', self.__xpath_number, "Auth form login")

    def get_civil_main(self):
        return self.is_visible('xpath', self.__xpath_main, "Auth form login")

    def get_civil_paydays(self):
        return self.is_visible('xpath', self.__xpath_paydays, "Auth form login")

    def get_civil_price(self):
        return self.is_visible('xpath', self.__xpath_price, "Auth form login")

    def get_civil_extra(self):
        return self.is_visible('xpath', self.__xpath_extra, "Auth form login")

    def get_civil_company(self):
        return self.is_visible('xpath', self.__xpath_company, "Auth form login")

    def get_civil_adr(self):
        return self.is_visible('xpath', self.__xpath_adr, "Auth form login")

    def get_civil_checkbox(self):
        return self.is_visible('xpath', self.__xpath_checkbox, "Auth form login")

    def get_civil_id(self):
        return self.is_visible('xpath', self.__xpath_id, "Auth form login")

    def get_civil_bank_name(self):
        return self.is_visible('xpath', self.__xpath_bank_name, "Auth form login")

    def get_civil_bik(self):
        return self.is_visible('xpath', self.__xpath_bik, "Auth form login")

    def get_civil_iik(self):
        return self.is_visible('xpath', self.__xpath_iik, "Auth form login")

    def get_civil_owner(self):
        return self.is_visible('xpath', self.__xpath_owner, "Auth form login")

    def get_civil_owner_phone(self):
        return self.is_visible('xpath', self.__xpath_owner_phone, "Auth form login")

    def get_civil_employer(self):
        return self.is_visible('xpath', self.__xpath_employer, "Auth form login")

    def get_civil_employer_addr(self):
        return self.is_visible('xpath', self.__xpath_employer_addr, "Auth form login")

    def get_civil_employer_reg(self):
        return self.is_visible('xpath', self.__xpath_employer_reg, "Auth form login")

    def get_civil_employer_id(self):
        return self.is_visible('xpath', self.__xpath_employer_id, "Auth form login")

    def get_civil_employer_iin(self):
        return self.is_visible('xpath', self.__xpath_employer_iin, "Auth form login")

    def get_civil_bank(self):
        return self.is_visible('xpath', self.__xpath_employer_bank, "Auth form login")

    def get_civil_bill(self):
        return self.is_visible('xpath', self.__xpath_employer_bill, "Auth form login")

    def get_civil_employer_phone(self):
        return self.is_visible('xpath', self.__xpath_employer_phone, "Auth form login")

    def get_accept_button(self):
        return self.is_visible('xpath', self.__xpath_accept_button, "Auth form login")
