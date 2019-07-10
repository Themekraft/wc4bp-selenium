from selenium.webdriver.common.by import By

from BuddyForms.utils.Utils import Utils


class LoginPage(Utils):
    """ Locators """
    username_email_field = By.ID, "user_login"
    password_field = By.ID, "user_pass"
    log_in_button = By.ID, "wp-submit"
    """ End of Locators """

    """ Credentials """
    username = "njota08@gmail.com"
    password = "Ofj!RFc(S6k!31SC15hR@s9n"

    def login_process(self):
        Utils.wait_visibility_element_send_keys(self, self.username_email_field, self.username)
        Utils.wait_visibility_element_send_keys(self, self.password_field, self.password)
        Utils.wait_clickable_element_and_click(self, self.log_in_button)
