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
    _course = "course-listing-title" # class
    _all_courses = "//a[contains(text(),'All Courses')]" # xpath
    _enroll_button = "enroll-button-top"
    _pay_pal = "paypal-radio" # id
    _cc_num = "cardnumber" # name
    _cc_exp = "expiration" # id
    _cc_cvv = "cvc" # name
    _submit_enroll = "//button[@id='confirm-purchase']/label" # xpath
    _enroll_error_message = ""


    def enterCourseName(self, name):
        self.elementClick(self._all_courses, locatorType="xpath")
        self.sendKeys(name, self._search_box, locatorType="name")

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick()

    def enterCardNum(self, num):
        pass

    def enterCardExp(self, exp):
        pass

    def enterCardCVV(self, cvv):
        pass

    def clickEnrollSubmitButton(self):
        pass

    def enterCreditCardInformation(self, num, exp, cvv):
        pass

    def enrollCourse(self, num="", exp="", cvv=""):
        pass

    def verifyEnrollFailed(self):
        pass
