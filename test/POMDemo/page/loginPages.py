
from test.POMDemo.locators.locators import Locators

class LoginPage():

    """This class will check specifically 4C Insights Login page """

    def __init__(self, driver):
        self.driver = driver

        # assigning variables
        self.login_page_xpath = Locators.login_page_xpath
        self.username_insight_id = Locators.username_insight_id
        self.password_insight_id = Locators.password_insight_id
        self.login_button_xpath = Locators.login_button_xpath
        self.error_message_xpath= Locators.error_message_xpath

    # Login button in Main page will be clicked
    def click_login_page(self):
        self.driver.find_element_by_xpath(self.login_page_xpath).click()

    # Username will be cleared & new Username will be send
    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_insight_id).clear()
        self.driver.find_element_by_id(self.username_insight_id).send_keys(username)

    # Password will be cleared and new Password will be send
    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_insight_id).clear()
        self.driver.find_element_by_id(self.password_insight_id).send_keys(password)

    # Login Button will be clicked
    def click_login (self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    #"Specified user does not exist"--> error text should be returned
    def check_error_message(self):
        msg = self.driver.find_element_by_xpath(self.error_message_xpath).text
        return msg