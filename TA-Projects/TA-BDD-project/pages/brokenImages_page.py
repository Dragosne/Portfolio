from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import requests

class BrokenImages(BasePage):

    # page url
    BROKEN_IMAGES_URL = 'https://the-internet.herokuapp.com/broken_images'

    # selector parts
    IMAGES_SELECTOR = (By.TAG_NAME, 'img')

    # method parts
    def navigate_to_the_url(self):
        self.driver.get(self.BROKEN_IMAGES_URL)

    def wait_for_page_loading(self):
        return self.wait_until_is_displayed(self.IMAGES_SELECTOR, 6)

    def check_for_broken_images(self):
        # identify all image type elements using tag <img> from the page
        images = self.driver.find_elements(*self.IMAGES_SELECTOR)

        # create a list to keep the broken images
        broken_images = []

        # iterate through images and check the status
        for image in images:
            # Get images url
            image_url = image.get_attribute('src')

            # check the image status using HTTP request (install request!!!)
            response = requests.get(image_url)

            # filter the response and add the broken images url's
            if response.status_code != 200:
                broken_images.append(image_url)

        return broken_images
