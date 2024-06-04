from driver import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BasePage(Driver):

    # click method
    def click(self, locator):
        self.driver.find_element(*locator).click()

    # find element method
    def element_selector(self, locator):
        return self.driver.find_element(*locator)

    # input text method
    def type(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    # wait for element presence method
    def wait_for_element(self, locator, wait_time) -> WebElement:
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.presence_of_element_located(locator))

    # get text
    def get_element_text(self, locator):
        return self.wait_for_element(locator, 10).text

    # select method
    def select_dropdown(self, locator):
        return Select(self.driver.find_element(*locator))

    # select dropdown option method
    def switch_dropdown(self, locator, option):
        return self.select_dropdown(locator).select_by_visible_text(option)

    # wait for element visibility method
    def wait_for_visibility(self, locator, wait_time):
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.visibility_of_element_located(locator))

    # wait until element is displayed method
    def wait_until_is_displayed(self, locator, wait_time):
        return self.wait_for_element(locator, wait_time).is_displayed()
