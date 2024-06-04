from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ChallengingDOM(BasePage):

    # page url
    CHALLENGING_DOM_URL = "https://the-internet.herokuapp.com/challenging_dom"

    # selectors part
    # different elements from webpage table with different selectors
    IUARVET1 = (By.CSS_SELECTOR, 'div.large-10.columns tbody tr:nth-of-type(2) td:nth-of-type(1)')
    IUARVET7 = (By.CSS_SELECTOR, 'div.large-10.columns tbody tr:nth-of-type(8) td:nth-of-type(1)')
    DEFINIEBAS5 = (By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[6]/td[4]")
    ADIPISCI5 = (By.XPATH, '//*[@id="content"]/div/div/div/div[2]/table/tbody/tr[6]/td[3]')
    CONSEQUUNTUR5 = (By.XPATH, '//td[contains(text(), "Consequuntur5")]')

    # buttons selectors
    FIRST_BUTTON_SELECTOR = (By.CSS_SELECTOR, 'div.large-2.columns a:nth-of-type(1)')
    SECOND_BUTTON_SELECTOR = (By.CSS_SELECTOR, 'div.large-2.columns a:nth-of-type(2)')
    THIRD_BUTTON_SELECTOR = (By.CSS_SELECTOR, 'div.large-2.columns a:nth-of-type(3)')

    # canvas selector
    CANVAS = (By.ID, 'canvas')

    # method parts
    def navigate_to_challengingDOM_webpage(self):
        self.driver.get(self.CHALLENGING_DOM_URL)

    def select_element_and_get_text(self, element_name):
        # a dictionary with all selected elements and selectors
        elements_map = {
            "Iuvaret1": self.IUARVET1,
            "Iuvaret7": self.IUARVET7,
            "Definiebas5": self.DEFINIEBAS5,
            "Adipisci5": self.ADIPISCI5,
            "Consequuntur5": self.CONSEQUUNTUR5,
        }
        # check if the element_name is present in elements map
        if element_name in elements_map:
            selected_element = elements_map[element_name]
            element_text = self.get_element_text(selected_element)
            return element_text
        else:
            element_text = f"found {element_name} that does not exist or is out of test scope"
            return element_text

    def canvas_status(self):
        canvas = self.element_selector(self.CANVAS)

        # identify canvas 2d drawing context
        context = self.driver.execute_script('return arguments[0].getContext("2d");', canvas)

        # identify the status of the 2d canvas context
        canvas_status = self.driver.execute_script('return arguments[0].canvas;', context)
        return canvas_status

    def click_button(self, button_number):
        # create a map of buttons and selectors
        buttons_map = {
            "1st": self.FIRST_BUTTON_SELECTOR,
            "2nd": self.SECOND_BUTTON_SELECTOR,
            "3rd": self.THIRD_BUTTON_SELECTOR
        }

        # check if the button_number is in defined map
        if button_number in buttons_map:
            selected_button = buttons_map[button_number]
            self.click(selected_button)
        else:
            print(f"The button_number {button_number} is not defined")