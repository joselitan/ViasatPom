from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import Status
import unittest
import pytest
from locators.locators import Locators
import time

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class RegisterCoursesTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    def test_validEnrollment(self):
        self.courses.clickAllCourses()
        self.courses.enterCourseName(Locators.course_name)
        self.courses.selectCourseToEnroll(Locators.select_course)
        #testing
        """
        https://www.google.com/search?q=python+selenium+copy+paste+text&oq=selenium+python+copy+paste&aqs=chrome.1.69i57j0.11611j0j7&sourceid=chrome&ie=UTF-8
        """
        self.courses.enrollCourse(num=Locators.card_number, exp="0925", cvv="111", postal="12210")
