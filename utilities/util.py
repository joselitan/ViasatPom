"""
@package utilities

Util class implementation
All most commonly used utilities should be implemented in this class

Example:
    name = self.util.getUniqueName()
"""
import time
import traceback
import random, string
import utilities.custom_logger as cl
import logging

class Util(object):

    log = cl.customLogger(logging.INFO)

    def sleep(self, sec, info=""):
        """
        Put the program to wait for the specified amount of time
        """
        if info is not None:
            self.log.info("Wait :: '" + str(sec) + "' seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def getAlphaNumeric(self, length, type ="letters"):
        """
        Get random string of characters
        :param length: Length of string, number of characters string should have
        :param type: Type of characters string should have. Default is letters
        Provide lower/upper/digits for different types
        """

        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def getUniqueName(self, charCount=10):
        """
        Get a unique name
        """
        return self.getAlphaNumeric(charCount, 'lower')

    def getUniqueNameList(self, listSize=5, itemLength=None):
        """
        Get a list of valid email ids

        Parameters:
            listSize: Number of names. Default is 5 names in a list
            itemLength: It should be a list containing number of items equal to the listSize
                        This determines the lenght of the each item in the list[1,2,3,4,5]
        """
        nameList = []
        for i in range(0, listSize):
            nameList.append(self.getUniqueName(itemLength[i]))
        return nameList


    def verifyTextContains(self, actualText, expectedText):
        """
        Verify actual text contains expected text string
        Parameters:
            expectedList: expected Text
            actualList: actual Text
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERICATION CONTAINS")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS!!!")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        """
        Verify actual text contains expected text string
        Parameters:
            expectedList: expected Text
            actualList: actual Text
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)
        if expectedText.lower() == actualText.lower():
            self.log.info("### VERICATION CONTAINS")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS!!!")
            return False