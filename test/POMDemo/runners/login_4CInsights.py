from selenium import webdriver
import time
import unittest
from test.POMDemo.drivers.Test_Data import TestData
from test.POMDemo.utils.utils import PASSWORD_4CInsight, URL_4CInsights, USERNAME_4CInsights
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from test.POMDemo.page.loginPages import LoginPage
import HtmlTestRunner


class loginTest(unittest.TestCase):
    """This class is the script of the Login page. Here we will be executed coding"""

    @classmethod
    def setUpClass(cls):
        # Setting up driver with TestData Class for the security purposes
        cls.driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTE_PATH)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # Using URL, USERNAME, PASSWORD from the utils package and sending to the web page
    def test_login_valid(self):
        driver = self.driver
        driver.get(URL_4CInsights)
        login = LoginPage(driver)
        login.click_login_page()
        time.sleep(2)
        login.enter_username(USERNAME_4CInsights)
        login.enter_password(PASSWORD_4CInsight)
        login.click_login()

        # Assertion
        message = driver.find_element_by_xpath("//span[@class='field-error']").text
        self.assertEqual(message, "Specified user does not exist")

        # Saving ScreenShot
        # Screenshot can be viewed in the runners package
        # Name of the screenshot file can be renamed
        self.driver.save_screenshot("ScreenShot0.png")

        # Printing Error Message Displayed
        print ('Displayed error message: ' + message)
        time.sleep(2)

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
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=TestData.REPORT_EXECUTE_PATH))
