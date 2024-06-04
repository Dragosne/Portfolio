import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BebeTeiCart(unittest.TestCase):
    # webpage URL
    URL = "https://comenzi.bebetei.ro/"

    # dashboard URL
    URL_DASHBOARD = "https://comenzi.bebetei.ro/dashboard"

    # Flow:
    # 1. Log in successfully to a registered account.
    # 2. Go to the cart, check if there are items in the cart, and delete them if any.
    #     -> check if the cart is indeed empty after deleting items
    # 3. Select a product using the menus: Produse -> Jocuri si Jucarii -> Jocuri -> Jocuri de societate.
    #    -> Click on the first product listed.
    #    -> Click and add one item to the cart.
    #    -> Store the title, price and quantity of the item.
    #    -> Check for the alert message confirming the item was successfully added to the cart.
    # 4. Select a product using the search functionality:
    #    -> Search for "jucarii".
    #    -> Click on the first product listed.
    #    -> Click and add one item to the cart.
    #    -> Store the title, price and quantity of the item.
    #    -> Check for the alert message confirming the item was successfully added to the cart.
    # 5. Click on "Cosul meu", check if there are two products:
    #    -> Collect the titles, prices and quantity of the items.
    #    -> Verify that the stored item information from the previous steps matches the items displayed in the cart.
    # 6. Verify the cart cost produse

    # selectors part
    ACCEPT_ALL_COOKIES = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    CONTUL_MEU_BUTTON_ELEMENT = (By.XPATH,
                                 "//div[@class='position-relative']//img[@class='me-1' and @alt='Contul meu']")
    EMAIL_INPUT_FIELD_ELEMENT = (By.ID, "auth-email")
    CONTINUA_BUTTON_ELEMENT = (By.ID, 'auth-next-btn')
    PASSWORD_INPUT_FIELD_ELEMENT = (By.CSS_SELECTOR, 'input.form-control#auth-login-password')
    CONECTEAZA_TE_BUTTON_ELEMENT = (By.ID, 'auth-next-btn')
    LOGOUT_BUTTON_ELEMENT = (By.XPATH, "//span[@class='me-1' and contains(text(), 'Deconectare')]")

    # selectors part
    # menu navigation
    PRODUSE_ELEMENT = (By.XPATH, '//a[@class="js-desktop-menu-title"]/span[text()="Produse"]')
    JOCURI_SI_JUCARII_ELEMENT = (
        By.CSS_SELECTOR, 'a.d-inline-block.level-1-link[href="https://comenzi.bebetei.ro/jocuri-si-jucarii/"]')
    JOCURI_ELEMENT = (
        By.CSS_SELECTOR, 'a.d-inline-block.level-2-link[href="https://comenzi.bebetei.ro/jocuri-si-jucarii/jocuri/"]')
    JOURI_DE_SOCIETATE_ELEMENT = (By.CSS_SELECTOR,
                                  'a.d-inline-block[href="https://comenzi.bebetei.ro/jocuri-si-jucarii/jocuri/jocuri-de-societate/"]')

    # buttons
    COSUL_MEU_BUTTON_ELEMENT = (By.ID, 'top-cart-btn')
    COS_CUMPARATURI_ELEMENTS = (By.CSS_SELECTOR, 'div.align-items-center.cart_product.d-flex')

    DELETE_CART_ITEM_ELEMENT = (By.CSS_SELECTOR, 'a.d-inline-block.js-remove-item.text-muted')
    CONTINUA_CUMPARATURILE_BUTTON_ELEMENT = (By.CSS_SELECTOR, 'a[href="https://comenzi.bebetei.ro/"]')
    DA_DELETE_BUTTON_ELEMENT = (By.XPATH, '//div[@class="jconfirm-buttons"]//button[text()="Da"]')
    CUMPARA_BUTTON_ELEMENT = (By.CSS_SELECTOR, 'a[href="https://comenzi.bebetei.ro/cart"]')

    SEARCH_FIELD_ELEMENT = (By.ID, 'desktop-search')
    SUBMIT_SEARCH_BUTTON_ELEMENT = (By.ID, 'submit-button')

    TOTAL_COS_CUMPARATURI_ELEMENT = (By.CSS_SELECTOR, 'div.total-info.mb-3 > h2.cart_total')
    COST_PRODUSE_ELEMENT = (By.CSS_SELECTOR, 'div#products-total > div.d-flex.justify-content-between > span:nth-of-type(2)')
    FIRST_PRODUCT_LISTED_ELEMENT = (By.CSS_SELECTOR, "div.product-item.product-details")
    ADD_TO_CART_BUTTON_ELEMENT = (By.ID, 'add-to-cart-btn')

    # product info titles, prices, containers
    PRODUCT_TITLE_ELEMENT = (By.CSS_SELECTOR, "h1#product-h1")
    PRODUCT_PRICE_ELEMENT = (By.CSS_SELECTOR, 'div.price-info.mb-2 > div.regular-price')

    PRICE_CART_CONTAINER = (By.CSS_SELECTOR, "div.product-subtotal")
    CART_ITEMS_CONTAINER = (By.CSS_SELECTOR, "div.cart_product")
    PRODUCT_ADDED_ALERT_CONTAINER = (By.CSS_SELECTOR, "div.pnotify-text > span.pnotify-pre-line")
    CART_TITLES_ATTRIBUTE = "data-product-name"

    # expected messages
    PRODUCT_ADDED_EXPECTED_MESSAGE = 'Produsul a fost adaugat cu succes in cos.'

    # other inputs
    # positive credentials
    EMAIL_POSITIVE_INPUT = "dragos.nechifor@nechys.com"
    USER_NAME = "Dragos Ionel"
    PASSWORD_POSITIVE_INPUT = "@Parola2024"

    # product search
    PRODUCT_SEARCH_INPUT = "Jucarii"

    @classmethod
    def setUpClass(cls):
        # class variables for storing product title price and quantity
        cls.first_product_info = {}
        cls.second_product_info = {}
        cls.found_products = {}

    def setUp(self):
        # setup browser, url and required wait time
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def helper_accept_all_cookies(self):
        # click to accept all cookies
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ACCEPT_ALL_COOKIES))
        self.driver.find_element(*self.ACCEPT_ALL_COOKIES).click()

    def helper_login(self):
        # login
        # click on contul meu
        self.driver.find_element(*self.CONTUL_MEU_BUTTON_ELEMENT).click()

        # input email and click
        input_email = self.driver.find_element(*self.EMAIL_INPUT_FIELD_ELEMENT)
        input_email.click()
        input_email.clear()
        input_email.send_keys(self.EMAIL_POSITIVE_INPUT)
        self.driver.find_element(*self.CONTINUA_BUTTON_ELEMENT).click()

        # input password and click
        input_password = self.driver.find_element(*self.PASSWORD_INPUT_FIELD_ELEMENT)
        input_password.click()
        input_password.clear()
        input_password.send_keys(self.PASSWORD_POSITIVE_INPUT)
        self.driver.find_element(*self.CONECTEAZA_TE_BUTTON_ELEMENT).click()

    def helper_go_to_cart(self):
        # cosul meu find element and click
        cosul_meu_button = self.driver.find_element(*self.COSUL_MEU_BUTTON_ELEMENT)
        cosul_meu_button.click()

        # cumpara find element and click
        cumpara_button = self.driver.find_element(*self.CUMPARA_BUTTON_ELEMENT)
        cumpara_button.click()

    def helper_empty_cart(self):
        # go to cart
        self.helper_go_to_cart()

        # find cart total element
        cart_products = self.driver.find_elements(*self.COS_CUMPARATURI_ELEMENTS)

        # if there are products left in your cart, delete them
        for product in cart_products:
            delete_product_button = self.driver.find_element(*self.DELETE_CART_ITEM_ELEMENT)
            delete_product_button.click()
            time.sleep(1)
            confirm_delete_button_yes = self.driver.find_element(*self.DA_DELETE_BUTTON_ELEMENT)
            confirm_delete_button_yes.click()
            time.sleep(1)

        # check if the cart is empty after deleting items
        cart_total = self.driver.find_element(*self.TOTAL_COS_CUMPARATURI_ELEMENT)
        cart_total_text = cart_total.text.split()[0].replace(",", ".")
        cart_total_value = float(cart_total_text)

        # assert the cart is empty
        self.assertEqual(cart_total_value, 0, "There are still items in the cart. Delete them and start the test again")

        # continua cumparaturile find element and click
        time.sleep(1)
        continua_cumparaturile_button = self.driver.find_element(*self.CONTINUA_CUMPARATURILE_BUTTON_ELEMENT)
        continua_cumparaturile_button.click()

    def test01_add_first_product_using_products_menu(self):
        # accept cookies, login and empty cart
        self.helper_accept_all_cookies()
        self.helper_login()
        self.helper_empty_cart()

        # navigate through the menus
        # produse find element and click
        produse_button = self.driver.find_element(*self.PRODUSE_ELEMENT)
        produse_button.click()

        # jocuri si jucarii find element and click
        jocuri_si_jucarii_button = self.driver.find_element(*self.JOCURI_SI_JUCARII_ELEMENT)
        jocuri_si_jucarii_button.click()

        # jocuri find element and click
        jocuri_button = self.driver.find_element(*self.JOCURI_ELEMENT)
        jocuri_button.click()

        # jocuri de societate find element and click
        jocuri_de_societate_button = self.driver.find_element(*self.JOURI_DE_SOCIETATE_ELEMENT)
        jocuri_de_societate_button.click()

        # find first listed element and click
        first_product = self.driver.find_element(*self.FIRST_PRODUCT_LISTED_ELEMENT)
        first_product.click()

        # find and store the product title, price
        first_product_title = self.driver.find_element(*self.PRODUCT_TITLE_ELEMENT)
        self.__class__.first_product_info['title'] = first_product_title.text

        first_product_price = self.driver.find_element(*self.PRODUCT_PRICE_ELEMENT)
        price = first_product_price.text.split()[0].replace(",", ".")
        price_value = float(price)
        self.__class__.first_product_info['price'] = price_value

        # add to cart find element and click to add one product
        add_to_cart_button = self.driver.find_element(*self.ADD_TO_CART_BUTTON_ELEMENT)
        add_to_cart_button.click()

        # assertion: product added to cart alert is displayed
        alert = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PRODUCT_ADDED_ALERT_CONTAINER))
        alert_text = alert.text
        self.assertIn(self.PRODUCT_ADDED_EXPECTED_MESSAGE, alert_text, f"The product does not added in cart")

        # store the quantity
        self.__class__.first_product_info['quantity'] = 1

    def test02_add_second_product_using_search(self):
        # accept cookies and login
        self.helper_accept_all_cookies()
        self.helper_login()

        # search field and submit button find elements
        search_field = self.driver.find_element(*self.SEARCH_FIELD_ELEMENT)
        submit_button = self.driver.find_element(*self.SUBMIT_SEARCH_BUTTON_ELEMENT)

        # action send product name and click for search
        search_field.click()
        search_field.clear()
        search_field.send_keys(self.PRODUCT_SEARCH_INPUT)

        submit_button.click()

        # find first listed element and click
        first_product = self.driver.find_element(*self.FIRST_PRODUCT_LISTED_ELEMENT)
        first_product.click()

        # find and store the product title, price
        second_product_title = self.driver.find_element(*self.PRODUCT_TITLE_ELEMENT)
        self.__class__.second_product_info['title'] = second_product_title.text

        second_product_price = self.driver.find_element(*self.PRODUCT_PRICE_ELEMENT)
        price = second_product_price.text.split()[0].replace(",", ".")
        price_value = float(price)
        self.__class__.second_product_info['price'] = price_value

        # add to cart find element and click to add one product
        add_to_cart_button = self.driver.find_element(*self.ADD_TO_CART_BUTTON_ELEMENT)
        add_to_cart_button.click()

        # assertion: product added to cart alert is displayed
        alert = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PRODUCT_ADDED_ALERT_CONTAINER))
        alert_text = alert.text
        self.assertIn(self.PRODUCT_ADDED_EXPECTED_MESSAGE, alert_text, f"The product does not added to cart")

        # store the quantity
        self.__class__.second_product_info['quantity'] = 1

    def test_03_check_the_cart_items_info(self):
        # accept cookies, login, go to cart
        self.helper_accept_all_cookies()
        self.helper_login()
        self.helper_go_to_cart()

        # extract product title and product price and store the values in a dict
        cart_items = self.driver.find_elements(*self.CART_ITEMS_CONTAINER)
        for product in cart_items:
            title = product.get_attribute(self.CART_TITLES_ATTRIBUTE)
            get_price = product.find_element(*self.PRICE_CART_CONTAINER).text.split()[0].replace(",", ".")
            price = float(get_price)
            get_quantity = product.find_element(By.CLASS_NAME, "pQuantity").get_attribute("value")
            quantity = int(get_quantity)
            self.found_products[title] = {"price": price, "quantity": quantity}

        # assertions: the info of previous added products (stored) are the same as the cart extracted info
        for product in [self.first_product_info, self.second_product_info]:
            title = product["title"]
            expected_price = product["price"]
            expected_quantity = product["quantity"]

            self.assertIn(title, self.found_products, f"The product {title} not found in cart")

            actual_price = self.found_products[title]["price"]
            actual_quantity = self.found_products[title]["quantity"]

            self.assertEqual(self.found_products[title]["price"], expected_price,
                             f"The price for the product {title} is not correct. "
                             f"Expected: {expected_price}, Found: {actual_price}")
            self.assertEqual(self.found_products[title]["quantity"], expected_quantity,
                             f"The quantity for the product {title} is not correct. "
                             f"Expected: {expected_quantity}, Found: {actual_quantity}")

    def test_04_check_the_cart_value(self):
        # accept cookies, loging, go to cart
        self.helper_accept_all_cookies()
        self.helper_login()
        self.helper_go_to_cart()

        # check the cart operations
        expected_products_total_cost = sum(self.found_products[title]['price'] * self.found_products[title]['quantity'] for title in self.found_products)
        total_cost = self.driver.find_element(*self.COST_PRODUSE_ELEMENT)
        actual_total_cost_displayed = float(total_cost.text.split()[0].replace(',', '.'))

        self.assertEqual(expected_products_total_cost, actual_total_cost_displayed,
                         f"The total cart value is not correct. Expected: {expected_products_total_cost}, Found: {actual_total_cost_displayed}")

