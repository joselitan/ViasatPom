from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"
    _user_setting = "//*[@id='navbar']//span[text()='Test User']"
    _invalid_credentials = ".//div[contains(text(),'Invalid email or password')]"

    def clickLoginLink(self):

        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):

        self.sendKeys(email, self._email_field)
        self.log.info("Entering: " + email)

    def enterPassword(self, password):

        self.sendKeys(password, self._password_field)
        self.log.info("Entering password")

    def clickLoginButton(self):

        self.elementClick(self._login_button, locatorType="name")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        # from time import sleep
        # sleep(2)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):

        result = self.isElementPresent(self._user_setting,
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):

        result = self.isElementPresent(self._invalid_credentials,
                                       locatorType="xpath")
        return result

    def clearFields(self):
        emailField = self.getElement(self._email_field)
        emailField.clear()
