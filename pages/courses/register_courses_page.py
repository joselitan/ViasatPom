import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_box = "query" #name
    # _course = "//div[contains(@class='course-listing-title') and contains(text(),'{0}')]" # xpath
    _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _all_courses = "//a[contains(text(),'All Courses')]" # xpath
    _enroll_button = "enroll-button-top"
    _cc_num = "cardnumber" # name
    _cc_exp = "expiration" # id
    _cc_cvv = "cvc" # name
    _submit_enroll = "//button[@id='confirm-purchase']/label" # xpath
    _enroll_error_message = ""
    _payment_information = "//h1[text()='Payment Information']"

    def clickAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="xpath")

    def enterCourseName(self, name):

        self.sendKeys(name, locator=self._search_box, locatorType="name")

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator = self._course.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button)

    def enterCardNum(self, num):
        self.sendKeys(num, locator=self._cc_num, locatorType="name")

    def enterCardExp(self, exp):
        self.sendKeys(exp, locator=self._cc_exp)

    def enterCardCVV(self, cvv):
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="cvc")


    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv)


    def verifyEnrollFailed(self):
        pass
