from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LogoutPage(BasePage):

    # selectors part
    LOGOUT_BUTTON = (By.XPATH, "//i[contains(text(), 'Logout')]")
    LOGOUT_FLASH_CONTAINER = (By.ID, "flash")
    PAGE_NAME_CONTAINER = (By.CLASS_NAME, "example")

    # methods part
    def click_logout(self):
        self.click(self.LOGOUT_BUTTON)

    def is_logout_message_displayed(self):
        return self.wait_until_is_displayed(self.LOGOUT_FLASH_CONTAINER, 6)

    def get_logout_message_text(self):
        return self.get_element_text(self.LOGOUT_FLASH_CONTAINER)

    def get_login_page_text(self):
        self.wait_until_is_displayed(self.PAGE_NAME_CONTAINER, 6)
        return self.get_element_text(self.PAGE_NAME_CONTAINER)
