from test.POMDemo.locators.locators import Locators


class Gmail_acc_page():

    # constructor
    def __init__(self, driver):
        self.driver = driver

        # assigning gmail webElement locators
        self.first_name_xpath = Locators.first_name_xpath
        self.last_name_xpath = Locators.last_name_xpath
        self.username_gmail_xpath = Locators.username_gmail_xpath
        self.password_gmail_xpath = Locators.password_gmail_xpath
        self.confirm_password_xpath = Locators.confirm_password_xpath
        self.next_button_xpath = Locators.next_button_xpath
        self.phone_number_id = Locators.phone_number_id
        self.verify_phone_num_text_xpath = Locators.verify_phone_num_text_xpath
        self.error_message_xpath =Locators.err_mess_phone_xpath

    def enter_first_name(self, gmailUser):
        self.driver.find_element_by_xpath(self.first_name_xpath).clear()
        self.driver.find_element_by_xpath(self.first_name_xpath).send_keys(gmailUser)

    def enter_last_name(self, gmailLast):
        self.driver.find_element_by_xpath(self.last_name_xpath).clear()
        self.driver.find_element_by_xpath(self.last_name_xpath).send_keys(gmailLast)

        # Username will be cleared & new Username will be send
    def enter_gmail_username(self, gmail_username):
        self.driver.find_element_by_xpath(self.username_gmail_xpath).clear()
        self.driver.find_element_by_xpath(self.username_gmail_xpath).send_keys(gmail_username)

        # Password will be cleared and new Password will be send
    def enter_gmail_password(self, gmail_password):
        self.driver.find_element_by_xpath(self.password_gmail_xpath).clear()
        self.driver.find_element_by_xpath(self.password_gmail_xpath).send_keys(gmail_password)

    def confirm_gmail_password(self, gmail_password_confirm):
        self.driver.find_element_by_xpath(self.confirm_password_xpath).clear()
        self.driver.find_element_by_xpath(self.confirm_password_xpath).send_keys(gmail_password_confirm)

    # Login Button will be clicked
    def click_next_button(self):
        self.driver.find_element_by_xpath(self.next_button_xpath).click()

    # verify phone number text message appears
    def verification_text(self):
        verify_mss = self.driver.find_element_by_xpath(self.verify_phone_num_text_xpath).text
        return verify_mss

    # send phone number to the input bar
    def number_enter(self, phone_number):
         self.driver.find_element_by_id(self.phone_number_id).send_keys(phone_number)

    # validate error message under the phone number input bar
    def error_message_text (self):
        err_message = self.driver.find_element_by_xpath(self.error_message_xpath).text
        return err_message