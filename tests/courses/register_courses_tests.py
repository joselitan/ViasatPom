from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import Status
import unittest
import pytest
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
        self.courses.enterCourseName('Javascript')
        time.sleep(2)
        self.courses.selectCourseToEnroll('JavaScript for beginners')
        self.courses.enrollCourse(num="4035300539804083", exp="0925", cvv="111")
