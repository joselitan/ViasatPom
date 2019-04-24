from pages.home.login_page import LoginPage
from utilities.teststatus import Status
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyLoginTitle()
        # assert result1 == True
        self.ts.mark(result1, "Title is incorrect")
        result2 = self.lp.verifyLoginSuccessful()
        # assert result2 == True
        self.ts.markFinal("test_validLogin", result2, "login was not successful")


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.clickLoginLink()
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True