from pages.loginLink.click_loginLink_page import ClickLoginPage
from utilities.teststatus import Status
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.clp = ClickLoginPage(self.driver)
        # self.ts = Status(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.clp.clogin()
