import unittest
import time
from selenium import webdriver
from BuddyForms.utils.Urls import Urls


class TestTemplate(unittest.TestCase):

    def setUp(self):
        """ Modify the WebDriver location path if needed.
        I'm looking for another option to avoid this """
        self.driver = webdriver.Chrome("C:/Users/Njota/PycharmProjects/Themekraft/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(Urls.wordpress_admin_page_apache_auth)
        time.sleep(5)

    def tearDown(self):
        if self.driver is not None:
            self.driver.quit()
