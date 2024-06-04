import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestBebeTeiLoginRegisteredUserPositive(unittest.TestCase):
    # webpage URL
    URL = "https://comenzi.bebetei.ro/"

    # flow: navigate to url -> click on contul meu button -> Input your email! webpage opening
    # input positive (registered) email -> click continua button -> Input your password! page opening
    # input positive password -> click Conecteaza-te button

    # testing webpages messages
    # testing checkboxes

    # selectors part and exepected messages
    # homepage selectors
    ACCEPT_ALL_COOKIES = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    CONTUL_MEU_BUTTON_ELEMENT = (By.XPATH,
                                 "//div[@class='position-relative']//img[@class='me-1' and @alt='Contul meu']")

    # Input your email! webpage
    # fields and buttons selectors
    EMAIL_INPUT_FIELD_ELEMENT = (By.ID, "auth-email")
    CONTINUA_BUTTON_ELEMENT = (By.ID, 'auth-next-btn')
    # messages containers selectors
    INPUT_YOUR_EMAIL_WEBPAGE_MESSAGE_CONTAINER = (By.ID, 'step-email-txt')
    # webpage expected title
    INPUT_EMAIL_WEBPAGE_EXPECTED_MESSAGE = 'Introduceți adresa de email:'

    # Input you password! webpage
    # fields and buttons selectors
    PASSWORD_INPUT_FIELD_ELEMENT = (By.CSS_SELECTOR, 'input.form-control#auth-login-password')
    CHECKBOX_MENTINE_CONECTAT_ELEMENT = (By.ID, 'auth-remember-me')
    AI_UITAT_PAROLA_ELEMENT = (By.ID, 'auth-forgot-password-btn')
    CONECTEAZA_TE_BUTTON_ELEMENT = (By.ID, 'auth-next-btn')
    INAPOI_BUTTON_ELEMENT = (By.CSS_SELECTOR, 'a.link')
    # messages containers selectors
    INPUT_YOUR_PASSWORD_WEBPAGE_MESSAGE_CONTAINER = (By.CSS_SELECTOR, "p.js-intro-txt#step-login-txt")
    # webpage expected title
    INPUT_PASSWORD_WEBPAGE_EXPECTED_MESSAGE = 'Introduceți parola pentru a vă putea conecta.'

    # Ai uitat parola webpage
    # webpage name message container
    AI_UITAT_PAROLA_MESSAGE_CONTAINER = (By.ID, 'auth-forgot-password-success')

    # webpage expected message
    AI_UITAT_PAROLA_EXPECTED_MESSAGE = ('V-am trimis un link de resetare a parolei. '
                                        'Verificați adresa de email introdusa anterior, '
                                        'inclusiv folderele Spam/Junk și urmați instrucțiunile!')

    # logged in message container
    SUCCESS_LOGIN_PAGE_MESSAGE_CONTAINER = (By.ID, 'header-links-left')

    # logged in successful expected welcome message
    SUCCESS_LOGIN_PAGE_EXPECTED_MESSAGE = 'Bun venit, <write here your account name and surname>!'

    # logged out selectors
    LOGOUT_BUTTON_ELEMENT = (By.XPATH, "//span[@class='me-1' and contains(text(), 'Deconectare')]")
    HOME_PAGE_EXPECTED_TITLE = "https://comenzi.bebetei.ro/"

    # other inputs
    # positive credentials
    EMAIL_POSITIVE_INPUT = "<write here your registered email>"
    USER_NAME = "<write here your account name and surname>"
    PASSWORD_POSITIVE_INPUT = "<write here your valid password>"

    # navigate to url -> accept cookies -> click on contul meu
    def setUp(self):
        # setup browser, url and required wait time
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.driver.implicitly_wait(5)
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
        actual_message = message.text
        expected_message = self.INPUT_EMAIL_WEBPAGE_EXPECTED_MESSAGE

        self.assertEqual(expected_message, actual_message,
                         f" We are not on the Input your email! webpage. "
                         f"The expected page name is '{expected_message}', "
                         f"but the actual page name is '{actual_message}'")

    def helper_pass_over_email_step(self):
        # find elements
        email_field = self.driver.find_element(*self.EMAIL_INPUT_FIELD_ELEMENT)
        continua_button = self.driver.find_element(*self.CONTINUA_BUTTON_ELEMENT)

        # action input wrong format email -> click continua button
        email_field.click()
        email_field.clear()
        email_field.send_keys(self.EMAIL_POSITIVE_INPUT)
        continua_button.click()

    def test02_input_positive_email_and_password_page_name(self):
        self.helper_pass_over_email_step()

        # assertion: we are on the Input you password! webpage & check the message
        time.sleep(1)  # is not working without this
        message = self.driver.find_element(*self.INPUT_YOUR_PASSWORD_WEBPAGE_MESSAGE_CONTAINER)
        actual_message = message.text
        expected_message = self.INPUT_PASSWORD_WEBPAGE_EXPECTED_MESSAGE

        self.assertEqual(expected_message, actual_message,
                         f" We are not on the Input your password! webpage. "
                         f"The expected page name is '{expected_message}', "
                         f"but the actual page name is '{actual_message}'")

    def test03_password_webpage_inapoi_button(self):
        self.helper_pass_over_email_step()

        # find elements
        inapoi_button = self.driver.find_element(*self.INAPOI_BUTTON_ELEMENT)

        # action click using JavaScript
        self.driver.execute_script("arguments[0].click();", inapoi_button)

        # inapoi_button.click() - not working

        # assertion: we are on the Input you email! webpage & check the message
        message = self.driver.find_element(*self.INPUT_YOUR_EMAIL_WEBPAGE_MESSAGE_CONTAINER)
        actual_message = message.text.replace('\n', ' ')
        expected_message = self.INPUT_EMAIL_WEBPAGE_EXPECTED_MESSAGE

        self.assertEqual(expected_message, actual_message,
                         f" We are not on the Input your email! webpage. "
                         f"The expected page name is '{expected_message}', "
                         f"but the actual page name is '{actual_message}'")

    def test04_mentine_conectat_checkbox(self):
        self.helper_pass_over_email_step()

        # find elements
        mentine_connectat_checkbox = self.driver.find_element(*self.CHECKBOX_MENTINE_CONECTAT_ELEMENT)

        # assertion: mentine conectat checkbox is not selected
        self.assertFalse(mentine_connectat_checkbox.is_selected(),
                         "Mentine conectat checkbox should be not selected but is selected")

        # click to select the checkbox
        mentine_connectat_checkbox.click()

        # assertion: mentine conectat checkbox is not selected after the user clicks to select it
        self.assertTrue(mentine_connectat_checkbox.is_selected(),
                        "Mentine conectat checkbox is not selected after the user clicks to select it")

        # click to deselect the checkbox
        mentine_connectat_checkbox.click()

        # assertion: mentine conectat checkbox is selected after the user clicks to deselect it
        self.assertFalse(mentine_connectat_checkbox.is_selected(),
                         "Mentine conectat checkbox is selected after the user clicks to deselect it")

    def test05_ai_uitat_parola_button(self):
        self.helper_pass_over_email_step()

        # Find elements
        ai_uitat_parola_button = self.driver.find_element(*self.AI_UITAT_PAROLA_ELEMENT)

        # Action: click ai uitat parola button
        ai_uitat_parola_button.click()
        time.sleep(2)  # not working without time sleep, neither webdriverwait

        # Assertion: we are on the Input your email! webpage & check the message
        message = self.driver.find_element(*self.AI_UITAT_PAROLA_MESSAGE_CONTAINER)
        actual_message = message.text.replace('\n', ' ')
        expected_message = self.AI_UITAT_PAROLA_EXPECTED_MESSAGE

        self.assertEqual(expected_message, actual_message,
                         f" We are not on the Ai uitat parola! webpage. "
                         f"The expected page name is '{expected_message}', "
                         f"but the actual page name is '{actual_message}'")

    def test06_login_into_account_positive_and_logout(self):
        self.helper_pass_over_email_step()

        # Find elements
        password_field = self.driver.find_element(*self.PASSWORD_INPUT_FIELD_ELEMENT)
        contecteaza_te_button = self.driver.find_element(*self.CONECTEAZA_TE_BUTTON_ELEMENT)

        # actions: input password and click conecteaza-te button
        password_field.click()
        password_field.clear()
        password_field.send_keys(self.PASSWORD_POSITIVE_INPUT)
        contecteaza_te_button.click()

        # assertion: we are logged in
        message = self.driver.find_element(*self.SUCCESS_LOGIN_PAGE_MESSAGE_CONTAINER)
        actual_message = message.text
        expected_message = self.SUCCESS_LOGIN_PAGE_EXPECTED_MESSAGE

        self.assertEqual(expected_message, actual_message,
                         f" We are not logged in your account. "
                         f"The expected welcome message is '{expected_message}', "
                         f"but the actual received message is '{actual_message}'")

        logout_button = self.driver.find_element(*self.LOGOUT_BUTTON_ELEMENT)
        logout_button.click()

        self.assertIn(self.HOME_PAGE_EXPECTED_TITLE, self.driver.current_url)
