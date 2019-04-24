"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Examples:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver
import os

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
             None
        """
        self.browser = browser
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/chromedriver/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration
        :return:
        """
        baseURL = "https://letskodeit.teachable.com/"
        # baseURL = "https://booking.viasat.tv/login"
        if self.browser == "iexplorer":
            # Set Ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            # chromedriver = "C:/chromedriver/chromedriver.exe"
            # os.environ["webdriver.chrome.driver"] = chromedriver
            # driver = webdriver.Chrome(chromedriver)
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Chrome()
        # Setting Driver Implicit Time Out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver


