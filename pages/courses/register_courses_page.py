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
    _course = "//div[@class='course-listing-title' and contains(text(),'JavaScript for beginners')]" # xpath
    #_course = "course-listing-title" # name
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
        self.log.info("Entering: " + name)

    def selectCourseToEnroll(self, fullCourseName):
        self.sendKeys(fullCourseName, self._search_box, locatorType="name")
        self.elementClick(self._course, locatorType="xpath")
        self.log.info("Selecting: " + fullCourseName)


    def enterCardNum(self, num):
        self.sendKeys(num, self._cc_num, locatorType="name")
        self.log.info("Entering card number: {num} ".format(num=num))

    def enterCardExp(self, exp):
        self.sendKeys(exp, self._cc_exp)
        self.log.info("Entering exp number: {exp} ".format(exp=exp))

    def enterCardCVV(self, cvv):
        self.sendKeys(cvv, self._cc_cvv, locatorType="cvc")
        self.log.info("Entering cvv: {cvv} ".format(cvv=cvv))

    def clickEnrollSubmitButton(self):
        self.elementClick(self._enroll_button)

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):

        self.clickEnrollSubmitButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv)


    def verifyEnrollFailed(self):
        pass
