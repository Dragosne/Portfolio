import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestBebeTeiLoginNewUser(unittest.TestCase):
    # website under test URL
    URL = "https://comenzi.bebetei.ro/"

    # flow:
    # navigate to url -> click on contul meu button -> Input your email! webpage opening
    # input (new user) email -> click continua button -> Complete the rest of new user data page opening
    # input username, password, reenter password, accept terms (checkbox) -> create new user button

    # testing webpages messages
    # testing each field positive/negative scenarios and checking the error messages and entire flow
    # will not click on create button to create new user account after the entire positive test

    # selectors part and expected messages
    # homepage selectors
    ACCEPT_ALL_COOKIES = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    CONTUL_MEU_BUTTON_ELEMENT = (By.XPATH,
                                 "//div[@class='position-relative']//img[@class='me-1' and @alt='Contul meu']")

    # Input your email! webpage
    # fields and buttons selectors
    EMAIL_INPUT_FIELD_ELEMENT = (By.ID, "auth-email")
    CONTINUA_BUTTON_ELEMENT = (By.ID, 'auth-next-btn')
    # messages containers selectors
    INPUT_YOUR_EMAIL_WEBPAGE_MESSAGE_CONTAINER = (By.ID, 'step-email-extra-message')
    EMAIL_FIELD_EMPTY_MESSAGE_CONTAINER = (By.ID, 'auth-no-email-error')
    EMAIL_FIELD_WRONG_INPUT_MESSAGE_CONTAINER = (By.ID, 'auth-email-error')
    # expected messages
    # the webpage
    INPUT_YOUR_EMAIL_WEBPAGE_EXPECTED_MESSAGE = 'Dacă nu aveți încă un cont, îl puteți crea în pasul următor.'
    # fields and buttons
    EMAIL_INPUT_FIELD_EMPTY_EXPECTED_MESSAGE = 'Trebuie să completezi o adresă de email pentru a putea continua!'
    EMAIL_INPUT_FIELD_WRONG_FORMAT_EXPECTED_MESSAGE = 'Adresa de email nu este validă'

    # Complete the rest of new user data! webpage
    # fields and buttons selectors
    NAME_INPUT_FIELD_ELEMENT = (By.ID, 'auth-name')
    PASSWORD_INPUT_FIELD_ELEMENT = (By.ID, 'auth-register-password')
    REENTER_PASSWORD_FIELD_ELEMENT = (By.ID, 'auth-register-password-confirm')
    TERMS_AND_CONDITIONS_CHECKBOX_ELEMENT = (By.ID, 'auth-terms-and-conditions')
    CREEAZA_CONT_BUTTON_ELEMENT = (By.ID, 'auth-next-btn-txt')
    # messages containers selectors
    REST_OF_DATA_WEBPAGE_MESSAGE_CONTAINER = (By.XPATH, '//p[@class="js-intro-txt" and @id="step-register-txt"]')
    PASSWORD_FIELD_MESSAGE_CONTAINER = (By.ID, 'auth-register-password-error')
    REENTER_PASSWORD_EMPTY_MESSAGE_CONTAINER = (By.ID, 'auth-register-password-confirm-error')
    REENTER_PASSWORD_FIELD_ERROR_MESSAGE_CONTAINER = (By.XPATH, '//p[contains(text(), "Parola nu se potriveste!")]')
    TERMS_AND_CONDITIONS_MESSAGE_CONTAINER = (By.ID, 'auth-terms-and-conditions-error')
    # expected messages
    # the webpage
    REST_OF_DATA_INPUT_EXPECTED_MESSAGE = 'Introduceți restul de date pentru a vă putea crea un cont nou:'
    # password field
    NO_CAPITAL_LETTER_EXPECTED_MESSAGE = "Parola trebuie sa contina cel putin 1 litere mari."
    NO_SMALL_LETTER_EXPECTED_MESSAGE = "Parola trebuie sa contina cel putin 1 litere mici."
    NO_NUMBERS_EXPECTED_MESSAGE = "Parola trebuie sa contina cel putin 1 cifre."
    NO_SPECIAL_CHAR_EXPECTED_MESSAGE = "Parola trebuie sa contina cel putin 1 caractere speciale."
    NO_8CHAR_EXPECTED_MESSAGE = "Parola trebuie sa contina cel putin 8 caractere."
    # reenter password field
    REENTER_PASSWORD_EMPTY_FIELD_EXPECTED_MESSAGE = "Confirmati parola"
    REENTER_DIFFERENT_PASSWORD_EXPECTED_MESSAGE = "Parola nu se potriveste!"
    TERMS_AND_CONDITIONS_NOT_ACCEPTED_EXPECTED_MESSAGE = ('Pentru a putea utiliza acest website trebuie sa fiti de '
                                                          'acord cu Termenii si Conditiile')

    # other inputs
    # positive credentials
    EMAIL_POSITIVE_INPUT = "dragosne@yahoo.com"
    USER_NAME_INPUT = "Dragos Nechifor"
    PASSWORD_POSITIVE_INPUT = "Parola@TMTA19"
    REENTER_PASSWORD_POSITIVE_INPUT = PASSWORD_POSITIVE_INPUT

    # negative credentials and inputs
    EMAIL_WRONG_FORMAT_INPUT = "dragos@mail"
    PASSWORD_NO_CAPITAL_LETTER_INPUT = "no_uppercase1!"
    PASSWORD_NO_SMALL_LETTER_INPUT = "NO_LOWERCASE1!"
    PASSWORD_NO_NUMBERS_INPUT = "No_Digits!"
    PASSWORD_NO_SPECIAL_CHAR_INPUT = "NoSpecial1"
    PASSWORD_NO_8CHAR_INPUT = "short"
    REENTER_PASSWORD_NEGATIVE_INPUT = "".join(reversed(PASSWORD_POSITIVE_INPUT))

    # navigate to url -> accept cookies -> click on contul meu
    def setUp(self):
        # setup browser, url and required wait time
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.driver.implicitly_wait(3)
        # click to accept all cookies
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ACCEPT_ALL_COOKIES))
        self.driver.find_element(*self.ACCEPT_ALL_COOKIES).click()
        # click on contul meu
        self.driver.find_element(*self.CONTUL_MEU_BUTTON_ELEMENT).click()

    def tearDown(self):
        self.driver.quit()

    def test01_input_your_email_page_expected_name(self):
        # assertion: we are on the Input you email! webpage & check the message
        message = self.driver.find_element(*self.INPUT_YOUR_EMAIL_WEBPAGE_MESSAGE_CONTAINER)
        actual_message = message.text.replace('\n', ' ')
        expected_message = self.INPUT_YOUR_EMAIL_WEBPAGE_EXPECTED_MESSAGE

        self.assertEqual(expected_message, actual_message,
                         f" We are not on the Input your email! webpage. "
                         f"The expected page name is '{expected_message}', "
                         f"but the actual page name is '{actual_message}'")

    def test02_input_your_email_empty_field_message(self):
        # find elements
        email_field = self.driver.find_element(*self.EMAIL_INPUT_FIELD_ELEMENT)
        continua_button = self.driver.find_element(*self.CONTINUA_BUTTON_ELEMENT)

        # action: empty email field (no input) -> click continua button
        email_field.click()
        email_field.clear()
        continua_button.click()

        # assertion: the expected message is displayed
        message = self.driver.find_element(*self.EMAIL_FIELD_EMPTY_MESSAGE_CONTAINER)
        actual_message = message.text
        expected_message = self.EMAIL_INPUT_FIELD_EMPTY_EXPECTED_MESSAGE

        self.assertEqual(expected_message, actual_message,
                         f"The error message received for empty password field is '{actual_message}', "
                         f"which differs from the expected message '{expected_message}'")

    def test03_input_your_email_wrong_format_message(self):
        # find elements
        email_field = self.driver.find_element(*self.EMAIL_INPUT_FIELD_ELEMENT)
        continua_button = self.driver.find_element(*self.CONTINUA_BUTTON_ELEMENT)

        # action input wrong format email -> click continua button
        email_field.click()
        email_field.clear()
        email_field.send_keys(self.EMAIL_WRONG_FORMAT_INPUT)
        continua_button.click()

        # assertion: the expected message is displayed
        message = self.driver.find_element(*self.EMAIL_FIELD_WRONG_INPUT_MESSAGE_CONTAINER)
        actual_message = message.text
        expected_message = self.EMAIL_INPUT_FIELD_WRONG_FORMAT_EXPECTED_MESSAGE

        self.assertEqual(expected_message, actual_message,
                         f"The error message received for wrong email format is '{actual_message}', "
                         f"which differs from the expected message '{expected_message}'")

    def helper_pass_over_email_step(self):
        # find elements
        email_field = self.driver.find_element(*self.EMAIL_INPUT_FIELD_ELEMENT)
        continua_button = self.driver.find_element(*self.CONTINUA_BUTTON_ELEMENT)

        # action input wrong format email -> click continua button
        email_field.click()
        email_field.clear()
        email_field.send_keys(self.EMAIL_POSITIVE_INPUT)
        continua_button.click()

    def test04_input_your_email_positive(self):
        self.helper_pass_over_email_step()

        # assertion: we pass over input email step - we are on the "Complete the rest of new user data! webpage"
        message = self.driver.find_element(*self.REST_OF_DATA_WEBPAGE_MESSAGE_CONTAINER)
        actual_message = message.text
        expected_message = self.REST_OF_DATA_INPUT_EXPECTED_MESSAGE

        self.assertEqual(expected_message, actual_message,
                         f" We are not on the Complete the rest of new user data! webpage")

    def test05_rest_user_data_webpage_expected_name(self):
        self.helper_pass_over_email_step()

        # assertion
        message = self.driver.find_element(*self.REST_OF_DATA_WEBPAGE_MESSAGE_CONTAINER)
        actual_message = message.text.replace('\n', ' ')
        expected_message = self.REST_OF_DATA_INPUT_EXPECTED_MESSAGE

        self.assertEqual(expected_message, actual_message,
                         f" We are not on the Complete the rest of new user data! webpage. "
                         f"The expected page name is '{expected_message}', "
                         f"but the actual page name is '{actual_message}'")

    def test06_input_wrong_format_new_user_password_messages(self):
        self.helper_pass_over_email_step()

        # define a map contains invalid password inputs and the expected messages for each
        invalid_passwords_error_messages_map = {
            self.PASSWORD_NO_8CHAR_INPUT: self.NO_8CHAR_EXPECTED_MESSAGE,
            self.PASSWORD_NO_SMALL_LETTER_INPUT: self.NO_SMALL_LETTER_EXPECTED_MESSAGE,
            self.PASSWORD_NO_CAPITAL_LETTER_INPUT: self.NO_CAPITAL_LETTER_EXPECTED_MESSAGE,
            self.PASSWORD_NO_NUMBERS_INPUT: self.NO_NUMBERS_EXPECTED_MESSAGE,
            self.PASSWORD_NO_SPECIAL_CHAR_INPUT: self.NO_SPECIAL_CHAR_EXPECTED_MESSAGE
        }

        # find element
        password_field = self.driver.find_element(*self.PASSWORD_INPUT_FIELD_ELEMENT)

        # input each invalid password and assert that the expected message is displayed
        for key, value in invalid_passwords_error_messages_map.items():
            # actions
            password_field.clear()
            password_field.click()
            password_field.send_keys(key)

            # get the message from website and the expected one from the map
            message = self.driver.find_element(*self.PASSWORD_FIELD_MESSAGE_CONTAINER)
            actual_message = message.text
            expected_message = value

            # assertion
            self.assertIn(expected_message, actual_message,
                          f"The error message received for wrong password input '{actual_message}' "
                          f"does not match the expected message '{expected_message}'")

    def helper_enter_username_and_password(self):
        # find elements
        username_field = self.driver.find_element(*self.NAME_INPUT_FIELD_ELEMENT)
        password_field = self.driver.find_element(*self.PASSWORD_INPUT_FIELD_ELEMENT)

        # actions: enter new username, password
        username_field.click()
        username_field.clear()
        username_field.send_keys(self.USER_NAME_INPUT)

        password_field.click()
        password_field.clear()
        password_field.send_keys(self.PASSWORD_POSITIVE_INPUT)

    def test07_reenter_password_empty_message(self):
        self.helper_pass_over_email_step()
        self.helper_enter_username_and_password()

        # find elements
        reenter_password_field = self.driver.find_element(*self.REENTER_PASSWORD_FIELD_ELEMENT)

        # actions: reenter password field empty
        reenter_password_field.click()
        reenter_password_field.clear()

        # assertion: the expected message is displayed
        message = self.driver.find_element(*self.REENTER_PASSWORD_EMPTY_MESSAGE_CONTAINER)
        actual_message = message.text
        expected_message = self.REENTER_PASSWORD_EMPTY_FIELD_EXPECTED_MESSAGE

        self.assertEqual(expected_message, actual_message,
                         f"The error message received for empty reenter password field is '{actual_message}', "
                         f"which differs from the expected message '{expected_message}'")

    def test08_reenter_password_wrong_input_message(self):
        self.helper_pass_over_email_step()
        self.helper_enter_username_and_password()

        # find elements
        reenter_password_field = self.driver.find_element(*self.REENTER_PASSWORD_FIELD_ELEMENT)

        # actions: reenter password field empty
        reenter_password_field.click()
        reenter_password_field.clear()
        reenter_password_field.send_keys(self.REENTER_PASSWORD_NEGATIVE_INPUT)

        # assertion: the expected message is displayed
        message = self.driver.find_element(*self.REENTER_PASSWORD_FIELD_ERROR_MESSAGE_CONTAINER)
        actual_message = message.text
        expected_message = self.REENTER_DIFFERENT_PASSWORD_EXPECTED_MESSAGE

        self.assertEqual(expected_message, actual_message,
                         f"The error message received for reentering different password is '{actual_message}', "
                         f"which differs from the expected message '{expected_message}'")

    def test09_terms_end_conditions_checkbox_not_selected_message(self):
        self.helper_pass_over_email_step()
        self.helper_enter_username_and_password()

        # find elements
        reenter_password_field = self.driver.find_element(*self.REENTER_PASSWORD_FIELD_ELEMENT)
        creeaza_cont_button = self.driver.find_element(*self.CREEAZA_CONT_BUTTON_ELEMENT)
        terms_checkbox = self.driver.find_element(*self.TERMS_AND_CONDITIONS_CHECKBOX_ELEMENT)

        # actions: reenter password
        reenter_password_field.click()
        reenter_password_field.clear()
        reenter_password_field.send_keys(self.REENTER_PASSWORD_POSITIVE_INPUT)

        # assertion: terms and conditions checkbox is not selected
        self.assertFalse(terms_checkbox.is_selected(),
                         "The terms and condition checkbox should be unselected but is selected")

        # click to select the checkbox
        terms_checkbox.click()

        # assertion: terms and conditions checkbox is selected after the user clicks to select it
        self.assertTrue(terms_checkbox.is_selected(),
                        "The terms and condition checkbox is not selected after the user clicks to select it")

        # click to deselect the checkbox
        terms_checkbox.click()

        # assertion: terms and conditions checkbox is selected after the user clicks to deselect it
        self.assertFalse(terms_checkbox.is_selected(),
                         "The terms and condition checkbox is selected after the user clicks to deselect it")

        if not terms_checkbox.is_selected():
            if not creeaza_cont_button.get_attribute("disabled"):
                creeaza_cont_button.click()

                # assertion: the expected message is displayed
                message = self.driver.find_element(*self.TERMS_AND_CONDITIONS_MESSAGE_CONTAINER)
                actual_message = message.text
                expected_message = self.TERMS_AND_CONDITIONS_NOT_ACCEPTED_EXPECTED_MESSAGE

                self.assertEqual(expected_message, actual_message,
                                 f"The error message received for clicking on 'creeaza cont' button"
                                 f" without accepting terms and conditions is '{actual_message}', "
                                 f"which differs from the expected message '{expected_message}'")
            else:
                print("Creeaza cont button is disabled. The error message displayed by clicking on creeaza cont "
                      "button without accepting the terms and condition can not be tested")

    def test10_login_new_user_positive(self):
        self.helper_pass_over_email_step()
        self.helper_enter_username_and_password()

        # find elements
        reenter_password_field = self.driver.find_element(*self.REENTER_PASSWORD_FIELD_ELEMENT)
        creeaza_cont_button = self.driver.find_element(*self.CREEAZA_CONT_BUTTON_ELEMENT)
        terms_checkbox = self.driver.find_element(*self.TERMS_AND_CONDITIONS_CHECKBOX_ELEMENT)

        # action: reenter password, accept terms and conditions
        # actions: reenter password
        reenter_password_field.click()
        reenter_password_field.clear()
        reenter_password_field.send_keys(self.REENTER_PASSWORD_POSITIVE_INPUT)
        terms_checkbox.click()

        # assertion: the create account button is active
        self.assertFalse(creeaza_cont_button.get_attribute("disabled"),
                         "The creeaza cont button is not active after positive scenario. "
                         "The new user account can not be created")
