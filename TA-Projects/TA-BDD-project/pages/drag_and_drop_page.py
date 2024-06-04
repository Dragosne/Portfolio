from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class DragDrop(BasePage):

    # page URL
    DRAG_AND_DROP_URL = "https://the-internet.herokuapp.com/drag_and_drop"

    #selectors part
    SOURCE_ELEMENT = (By.ID, 'column-a')
    TARGET_ELEMENT = (By.ID, 'column-b')

    # methods part
    def navigate_to_the_drag_and_drop_webpage(self):
        self.driver.get(self.DRAG_AND_DROP_URL)

    def source_element_state(self):
        return self.get_element_text(self.SOURCE_ELEMENT)

    def target_element_state(self):
        return self.get_element_text(self.TARGET_ELEMENT)

    # drag and drop action method using ActionChains
    def drag_and_drop_action(self):
        action = ActionChains(self.driver)
        action.drag_and_drop(self.element_selector(self.SOURCE_ELEMENT),
                             self.element_selector(self.TARGET_ELEMENT)).perform()
