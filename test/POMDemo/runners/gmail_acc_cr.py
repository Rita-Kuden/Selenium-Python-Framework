from selenium import webdriver
import time
import unittest
from test.POMDemo.drivers.Test_Data import TestData
from test.POMDemo.utils.utils import URL_gmail, PASSWORD_GMAIL, USERNAME_GMAIL, FIRST_NAME, LAST_NAME, PHONE_NUMBER
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from test.POMDemo.page.gmail_acc_page import Gmail_acc_page
import HtmlTestRunner

class gmail_Acc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setting up driver with TestData Class for the security purposes
        cls.driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTE_PATH)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()


    def test_create_acc(self):
        driver = self.driver
        driver.get(URL_gmail)
        driver.implicitly_wait(10)
        gmail_acc = Gmail_acc_page(driver)

        # first webpage opened
        gmail_acc.enter_first_name(FIRST_NAME)
        gmail_acc.enter_last_name(LAST_NAME)
        gmail_acc.enter_gmail_username(USERNAME_GMAIL)
        gmail_acc.enter_gmail_password(PASSWORD_GMAIL)
        gmail_acc.confirm_gmail_password(PASSWORD_GMAIL)
        gmail_acc.click_next_button()

        time.sleep(2)

        # second webPage with phone number
        gmail_acc.number_enter(PHONE_NUMBER)
        gmail_acc.click_next_button()

        time.sleep(2)

        # Validating text message displayed in the page
        mss = gmail_acc.verification_text()
        self.assertEqual(mss, "Verify your phone number")
        print ("Message displayed: " +mss)

        # Assertion error message
        err = gmail_acc.error_message_text()
        self.assertEqual(err, "This phone number format is not recognized. Please check the country and number.")
        print ("Displayed error message: " +err)
        self.driver.save_screenshot("ScreenShot1.png")

    @classmethod
    def tearDown(cls):
    # Driver will close after the test execution completes and "TEST COMPLETED" will be printed
        cls.driver.close()
        cls.driver.quit()
        print ("Test Completed")


if __name__ == '__main__':

    # Setting up our HTML reporting for passed and failed test.
    # This report can be found in the REPORTS package and can be opened in desired browser
    # Using Output path from TestData class for security purposes
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=TestData.REPORT_EXECURE_PATH))
