class UserData:
    phone = "7085898115"
    password = "NaN"


class SafeAuthPaths:
    phone = "/html/body/div[1]/div/div[2]/div[2]/div[3]/div/div/div[2]/form/div[1]/label/div/div[1]/div[2]/input"
    password = "/html/body/div[1]/div/div[2]/div[2]/div[3]/div/div/div[2]/form/div[2]/div[2]/label/div/div[1]/div[1]/input"
    sign_in = "/html/body/div[1]/div/div[2]/div[2]/div[3]/div/div/div[2]/form/div[3]/a"
    assertion = "/html/body/div[1]/div/div[1]/div/div/button/span[2]/span/span"
    logout = "/html/body/div[3]/div/div/a"
    logout_assert = "/html/body/div[1]/div/div[2]/div[2]/div[3]/div/div/div[1]/h3"


class SafeMainPage:
    seepact_path = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[3]/a"
    nda_path = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/a"
    teenacy_path = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/a"


class SafeNDAPage:
    accept = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[5]/button/span[2]/span"
    assertion = "/html/body/div[3]/div[2]/div/div/div/div[1]/div[1]/h3"


class SafeSeepactPage:
    get_name = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/label/div/div/div/input"
    button = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/button/span[2]/span"
    assertion = "/html/body/div[3]/div[2]/div/div/div/div[1]/div[1]/h3"


class SafeTenancyPage:
    accept = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/form/div[5]/button/span[2]/span  "
    assertion = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[3]/div/div/a[3]"


class SearchContractsPage:
    enum_contracts_class = "search_res"
    enum_page_class = "div[class='ac_table_block_text ac_tb_name']"


class DepositContractPage:
    xpath_next_button = "/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div[3]/button/span[2]/span"
    input_fields_selector = "input[class='q-field__native q-placeholder']"
    xpath_change = "//*[@id=\"q-app\"]/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div[3]/div/div/a[1]"


class MainPage:
    xpath_phone = "/html/body/div[3]/div[2]/div/div/div/div/div[2]/form/div[1]/label/div/div[1]/div[2]/input"
    xpath_password = "/html/body/div[3]/div[2]/div/div/div/div/div[2]/form/div[2]/div[" \
                     "2]/label/div/div/div[1]/input "
    xpath_next = "/html/body/div[3]/div[2]/div/div/div/div/div[2]/form/div[3]/a[2]"
    xpath_first = "/html/body/div[1]/div/div/div[2]/div[3]/div/div[3]/a"
    xpath_civil = "/html/body/div[1]/div/div/div[2]/div[2]/div[3]/div/div[2]/a"
    xpath_payday = "//*[@id=\"router-link\"]"
    xpath_my_templates = "/html/body/div[1]/div/nav/div[3]/ul/li[2]/a"
    xpath_labor = "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div/div[11]/div/div/a[2]"
    xpath_search = "/html/body/div[1]/div/nav/div[3]/ul/li[3]/a"
    xpath_new_pass = "/html/body/div[3]/div[2]/div/div/div/div/div[2]/form/div[4]/a"
    xpath_deposit_contract = "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div/div[1]/div/div/a"
    account_context = "button[class='q-btn q-btn-item non-selectable no-outline q-btn--unelevated " \
                      "q-btn--rectangle q-btn--actionable q-focusable q-hoverable q-btn-dropdown " \
                      "q-btn-dropdown--simple'] "
    xpath_logout = "/html/body/div[4]/div/div[2]/a[2]"
    feedback_name = "/html/body/div[1]/div/div[2]/div[1]/div[2]/div[4]/div[4]/div[4]/div/div[2]/div[1]/form/div[1]/div[1]/label/div/div/div/input"
    feedback_phone = "/html/body/div[1]/div/div[2]/div[1]/div[2]/div[4]/div[4]/div[4]/div/div[2]/div[1]/form/div[1]/div[2]/label/div/div[1]/div[2]/input"
    feedback_selectors = "input[class='q-field__native q-placeholder']"
    feedback_button = "/html/body/div[1]/div/div[2]/div[1]/div[2]/div[4]/div[4]/div[4]/div/div[2]/div[1]/form/div[2]/button"
    xpath_svg = "/html/body/div[1]/div/div/div[2]/div[4]/div[4]/div[4]/div/div[2]/div[2]/div[1]/div[1]/svg"
    xpath_auth_button = "/html/body/div[1]/div/div[1]/div/div/a"
