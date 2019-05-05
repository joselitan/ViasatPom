import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from time import sleep

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
    _cc_exp = "exp-date" # name
    _cc_cvv = "cvc" # name
    _cc_postal = "postal"
    _submit_enroll = "//button[@id='confirm-purchase']/label" # xpath
    _enroll_error_message = ""
    _payment_information = "//h1[text()='Payment Information']"
    _i_agree = "//div[@class='boolean-checkbox spc__checkbox spc__terms-text']//input[@type='checkbox']"

    def clickAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="xpath")

    def enterCourseName(self, name):

        self.sendKeys(name, locator=self._search_box, locatorType="name")

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator = self._course.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button)

    def enterCardNum(self, num):
        self.driver.switch_to.frame("__privateStripeFrame5")
        self.sendKeys(num, locator=self._cc_num, locatorType="name")
        self.driver.switch_to.default_content()

    def enterCardExp(self, exp):
        self.driver.switch_to.frame("__privateStripeFrame6")
        self.sendKeys(exp, locator=self._cc_exp, locatorType="name")
        self.driver.switch_to.default_content()

    def enterCardCVV(self, cvv):
        self.driver.switch_to.frame("__privateStripeFrame7")
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="name")
        self.driver.switch_to.default_content()

    def enterPostal(self, postal):
        self.driver.switch_to.frame("__privateStripeFrame8")
        self.sendKeys(postal, locator=self._cc_postal, locatorType="name")
        self.driver.switch_to.default_content()

    def click_agree(self):
        self.elementClick(locator=self._i_agree, locatorType="xpath")


    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")


    def enterCreditCardInformation(self, num, exp, cvv, postal):
        sleep(2)
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.enterPostal(postal)
        sleep(2)

    #def finalizePayment(self, ):


    def enrollCourse(self, num="", exp="", cvv="", postal=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv, postal)
        self.webScroll(direction="down")
        self.click_agree()

        #self.clickEnrollSubmitButton()


    def verifyEnrollFailed(self):
        pass
