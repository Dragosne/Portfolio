import os

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class JqueryMenu(BasePage):

    # page url
    JQUERY_URL = "https://the-internet.herokuapp.com/jqueryui/menu"

    # selectors part
    # main option enabled
    ENABLED_OPTION_1 = (By.ID, "ui-id-3")

    # enabled sub_options
    DOWNLOADS_OPTION_1_1 = (By.ID, "ui-id-4")
    BACK_TO_JQUERY_UI_OPTION_1_2 = (By.ID, 'ui-id-8')  # out of scope - not tested

    # downloads sub_options
    PDF_OPTION_1_1_1 = (By.ID, "ui-id-5")
    CSV_OPTION_1_1_2 = (By.ID, "ui-id-6")
    XLS_OPTION_1_1_3 = (By.ID, "ui-id-7")

    # other constants
    DEFAULT_DOWNLOAD_DIR = "/Users/nechiforos/Downloads"

    # methods part
    def navigate_to_jquery_webpage(self):
        self.driver.get(self.JQUERY_URL)

    def move_cursor_to_downloads(self):
        # action instance
        action = ActionChains(self.driver)

        # wait for required elements and move the mouse cursor
        self.wait_for_visibility(self.ENABLED_OPTION_1, 10)
        enable = self.element_selector(self.ENABLED_OPTION_1)
        action.move_to_element(enable).perform()

        self.wait_for_visibility(self.DOWNLOADS_OPTION_1_1, 10)
        downloads = self.element_selector(self.DOWNLOADS_OPTION_1_1)
        action.move_to_element(downloads).perform()

    def menu_options_map(self):
        # creating a map with downloads options
        file_type_map = {
            "PDF": self.PDF_OPTION_1_1_1,
            "CSV": self.CSV_OPTION_1_1_2,
            "Excel": self.XLS_OPTION_1_1_3
        }
        return file_type_map

    def move_mouse_cursor_to_file_type(self, sub_option):
        # find the required sub_option locator from created map
        selected_element = self.menu_options_map()[sub_option]
        action = ActionChains(self.driver)

        # wait for visibility
        self.wait_for_visibility(selected_element, 10)
        option = self.element_selector(selected_element)

        # move the mouse cursor to the required option
        action.move_to_element(option).perform()
        return option

    def check_filename_type_click_save_file(self, file_name, sub_option):
        # Check if the file exists in the default download directory
        downloaded_file_path = os.path.join(self.DEFAULT_DOWNLOAD_DIR, file_name)

        # if file exist, print an error message for the user
        if os.path.exists(downloaded_file_path):
            return False, f"The file {file_name} already exists in the Chrome default download directory.\n Please move or delete the file and run the test again!"

        # if not exist click and wait for download, check if the file has been saved and in the end delete the file
        else:
            # click to save the file
            self.move_mouse_cursor_to_file_type(sub_option).click()

            # wait to download the file using webdriver and a lambda function
            WebDriverWait(self.driver, 30).until(lambda parameter: os.path.exists(downloaded_file_path))

            # check if the file has been downloaded
            if not os.path.exists(downloaded_file_path):
                return False, "The download is not working, the file is not found in the download directory!"

            # remove the file from computer after the assertion
            os.remove(downloaded_file_path)
            return True, None

    # refresh webpage method for the next test
    def refresh_webpage(self):
        self.driver.refresh()

