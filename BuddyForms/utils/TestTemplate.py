import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.utils import Keys
from selenium.webdriver.common.actions.key_actions import KeyActions


class TestTemplate(unittest.TestCase):
    # APACHE AUTHENTICATION
    APACHE_USERNAME = "qa"
    APACHE_PASSWORD = "Q!W@E#R$T%"

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/Njota/PycharmProjects/Themekraft/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://buddyforms-premium.appscidentally.com/wp-admin")
        time.sleep(10)

    def tearDown(self):
        if self.driver is not None:
            self.driver.quit()
