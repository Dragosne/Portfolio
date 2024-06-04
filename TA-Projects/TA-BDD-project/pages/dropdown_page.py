from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class DropDown(BasePage):

    # page url
    DROPDOWN_URL = "https://the-internet.herokuapp.com/dropdown"

    # selectors part
    DROPDOWN = (By.ID, "dropdown")

    # methods part
    def navigate_to_the_dropdown_page(self):
        self.driver.get(self.DROPDOWN_URL)

    def check_dropdown_state(self):
        return self.select_dropdown(self.DROPDOWN).first_selected_option

    # get option value
    def get_dropdown_value(self):
        return self.check_dropdown_state().get_attribute("value")

    # switch between dropdown options
    def switch_dropdown_to_option(self, option):
        # find element and select first options
        self.switch_dropdown(self.DROPDOWN, option)

