import utilities.custom_logger as cl
from base.basepage import BasePage
import logging

class ClickLoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"

    def clickLoginLink(self):

        self.elementClick(self._login_link, locatorType="link")

    def clogin(self):

        self.clickLoginLink()