from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    # page URL
    LOGIN_PAGE_URL = "https://the-internet.herokuapp.com/login"

    # selectors part
    EMAIL_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//i[contains(text(),'Login')]")
    FLASH_CONTAINER = (By.ID, "flash-messages")

    # methods part
    def navigate_to_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def set_email(self, email):
        self.type(self.EMAIL_INPUT, email)

    def set_password(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def is_message_displayed(self):
        return self.wait_until_is_displayed(self.FLASH_CONTAINER, 6)

    def get_message_text(self):
        return self.get_element_text(self.FLASH_CONTAINER)