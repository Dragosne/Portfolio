from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AlertsPage(BasePage):
    # page url
    ALERTS_URL = "https://the-internet.herokuapp.com/javascript_alerts"

    # selectors part
    JS_ALERT_SELECTOR = (By.XPATH, "//button[contains(text(), 'Click for JS Alert')]")
    JS_CONFIRM_SELECTOR = (By.XPATH, "//button[contains(text(), 'Click for JS Confirm')]")
    JS_PROMPT_SELECTOR = (By.XPATH, "//button[contains(text(), 'Click for JS Prompt')]")
    RESULT_CONTAINER = (By.ID, 'result')

    # other constants
    JS_PROMPT_ALERT_TEXT_INPUT = "JavaScript"

    # Common methods
    def navigate_to_the_alerts_webpage(self):
        self.driver.get(self.ALERTS_URL)

    def alert_accept(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def alert_dismiss(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def get_result_text(self):
        self.wait_until_is_displayed(self.RESULT_CONTAINER, 6)
        return self.get_element_text(self.RESULT_CONTAINER)

    # Scenario: JS Alerts methods
    def click_on_JS_Alert_button(self):
        self.click(self.JS_ALERT_SELECTOR)

    def click_OK_on_JS_Alert_alert(self):
        self.alert_accept()

    # Scenario: JS Confirm methods
    def click_on_JS_Confirm_button(self):
        self.click(self.JS_CONFIRM_SELECTOR)

    def click_OK_on_JS_Confirm_alert(self):
        self.alert_accept()

    def click_CANCEL_on_JS_Confirm_alert(self):
        self.alert_dismiss()

    # Scenario: JS Prompt methods
    def click_on_JS_Prompt_button(self):
        self.click(self.JS_PROMPT_SELECTOR)

    def input_text_in_JS_Prompt_field(self):
        alert = self.driver.switch_to.alert
        alert.send_keys(self.JS_PROMPT_ALERT_TEXT_INPUT)

    def click_OK_on_JS_Prompt_alert(self):
        self.alert_accept()

    def click_CANCEL_on_JS_Prompt_alert(self):
        self.alert_dismiss()
