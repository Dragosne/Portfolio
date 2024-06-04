from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckBoxes(BasePage):

    # website url
    CHECKBOXES_URL = "https://the-internet.herokuapp.com/checkboxes"

    # checkboxes selectors
    CHECKBOX_1_SELECTOR = (By.CSS_SELECTOR, "form#checkboxes > input:nth-of-type(1)")
    CHECKBOX_2_SELECTOR = (By.CSS_SELECTOR, "form#checkboxes > input:nth-of-type(2)")

    # methods part
    def navigate_to_checkboxes_page(self):
        self.driver.get(self.CHECKBOXES_URL)

    def click_checkbox_1(self):
        self.click(self.CHECKBOX_1_SELECTOR)

    def click_checkbox_2(self):
        self.click(self.CHECKBOX_2_SELECTOR)

    def is_checkbox_1_selected(self):
        checkbox_1 = self.wait_for_element(self.CHECKBOX_1_SELECTOR,6)
        return checkbox_1.is_selected()

    def is_checkbox_2_selected(self):
        checkbox_2 = self.wait_for_element(self.CHECKBOX_2_SELECTOR, 6)
        return checkbox_2.is_selected()

