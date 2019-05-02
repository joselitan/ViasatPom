from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import Status
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class RegisterCoursesTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = Status(self.driver)

    def test_validEnrollment(self):
        self.courses.enterCourseName('Javascript')
        self.courses.selectCourseToEnroll('Javascript for beginners')
        self.courses.enrollCourse("4561540417529672", "11/22", "867")#("4561540417529672", "11/22", "867")
