from BuddyForms.utils.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    # Locators
    USERNAME_EMAIL_FIELD = "user_login"
    PASSWORD_FIELD = "user_pass"
    LOG_IN_BUTTON = "wp-submit"
    # Credentials
    USERNAME = "njota08@gmail.com"
    PASSWORD = "Ofj!RFc(S6k!31SC15hR@s9n"

    def login_process(self):
        self._driver.find_element_by_id(LoginPage.USERNAME_EMAIL_FIELD).send_keys(LoginPage.USERNAME)
        self._driver.find_element_by_id(LoginPage.PASSWORD_FIELD).send_keys(LoginPage.PASSWORD)
        self._driver.find_element_by_id(LoginPage.LOG_IN_BUTTON).click()
