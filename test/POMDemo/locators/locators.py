# Class is only for UI webElement locators
class Locators():
    # Login page objects
    login_page_xpath = "(//a[contains(text(),'Login')])[2]"
    username_insight_id = "email"
    password_insight_id = "password"
    login_button_xpath = "//input[@type='submit']"

    # error message
    error_message_xpath = "//span[@class='field-error']"

    # Gmail account credentials
    first_name_xpath = "//input[@aria-label = 'First name']"
    last_name_xpath = "//input[@aria-label = 'Last name']"
    username_gmail_xpath = "//input[@aria-label = 'Username']"
    password_gmail_xpath = "//input[@aria-label = 'Password']"
    confirm_password_xpath ="//input[@aria-label = 'Confirm']"
    next_button_xpath ="//span[contains(text(),'Next')]"
    phone_number_id ="phoneNumberId"
    verify_phone_num_text_xpath="//h1[contains(text(), 'Verify your phone number')]"
    verification_text_xpath ="//div[contains(text(),'Enter')]"
