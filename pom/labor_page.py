# Labor page object model

from base.selenium_base import SeleniumBase


class LaborPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.__xpath_name = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div[1]/label"
        self.__xpath_id = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div[" \
                          "3]/label/div/div/div/input "
        self.__xpath_date = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div[" \
                            "4]/label/div/div/div/input "
        self.__xpath_iin_or_rep = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div[" \
                                  "5]/label"
        self.__xpath_address = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div[6]/label"
        self.__xpath_address_reg = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div[" \
                                   "7]/label/div/div/div/input"
        self.__xpath_phone = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div[" \
                             "8]/label/div/div[1]/div[2]/input "
        self.__xpath_employee = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div[" \
                                "1]/label/div/div/div/input "

        self.__xpath_end_date = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div[3]/label"
        self.__xpath_start_date = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div[" \
                                  "4]/label/div/div/div/input "
        self.__xpath_time_first = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div[" \
                                  "5]/div[2]/label[1]/div/div/div/input "
        self.__xpath_time_second = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div[" \
                                   "5]/div[2]/label[2]/div/div/div/input "
        self.__xpath_time_third = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div[" \
                                  "6]/div[2]/label[1]/div/div/div/input "
        self.__xpath_time_last = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div[" \
                                 "6]/div[2]/label[2]/div/div/div/input "
        self.__xpath_vacation = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div[" \
                                "7]/label/div/div/div/input "
        self.__xpath_salary = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div[" \
                              "8]/label/div/div/div/input "
        self.__xpath_extra = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div[" \
                             "9]/label/div/div/div/input "
        self.__xpath_first_check = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div[" \
                                   "10]/div "
        self.__xpath_second_check = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div[" \
                                    "11]/div "
        self.__xpath_button = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/button/span[2]/span"
        self.css_change_button = "#q-app > div > div > div.admin_body > div > div.row.q-col-gutter-lg > div.col-12.col-lg-5 > div > div > div:nth-child(3) > div > div > a:nth-child(1)"

    def get_name(self):
        return self.is_visible('xpath', self.__xpath_name, "Input name")

    def get_id(self):
        return self.is_visible('xpath', self.__xpath_id, "Input identifier")

    def get_date(self):
        return self.is_visible('xpath', self.__xpath_date, "Input date")

    def get_iin_or_rep(self):
        return self.is_visible('xpath', self.__xpath_iin_or_rep, "Input iin")

    def get_address(self):
        return self.is_visible('xpath', self.__xpath_address, "Input address")

    def get_address_reg(self):
        return self.is_visible('xpath', self.__xpath_address_reg, "Input address reg")

    def get_phone(self):
        return self.is_visible('xpath', self.__xpath_phone, "Input phone")

    def get_employee(self):
        return self.is_visible('xpath', self.__xpath_employee, "Input employee")

    def get_end_date(self):
        return self.is_visible('xpath', self.__xpath_end_date, "Input date")

    def get_start_date(self):
        return self.is_visible('xpath', self.__xpath_start_date, "Input start date")

    def get_time_first(self):
        return self.is_visible('xpath', self.__xpath_time_first, "Input time")

    def get_time_second(self):
        return self.is_visible('xpath', self.__xpath_time_second, "Input time")

    def get_time_third(self):
        return self.is_visible('xpath', self.__xpath_time_third, "Input time")

    def get_time_last(self):
        return self.is_visible('xpath', self.__xpath_time_last, "Input time")

    def get_vacation(self):
        return self.is_visible('xpath', self.__xpath_vacation, "Input vacation")

    def get_salary(self):
        return self.is_visible('xpath', self.__xpath_salary, "Input salary")

    def get_extra(self):
        return self.is_visible('xpath', self.__xpath_extra, "Input extra")

    def get_first_check(self):
        return self.is_visible('xpath', self.__xpath_first_check, "First checkbox")

    def get_second_check(self):
        return self.is_visible('xpath', self.__xpath_second_check, "Second checkbox")

    def get_button(self):
        return self.is_visible('xpath', self.__xpath_button, "Done button")

    def get_change_button(self):
        return self.is_visible('css', self.css_change_button, "Done button")
