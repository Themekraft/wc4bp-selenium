import platform
import unittest
import time
from pathlib import Path

from selenium import webdriver
from BuddyForms.utils.Urls import Urls


class TestTemplate(unittest.TestCase):
    """ Operative System """
    os = platform.system()

    """ Webdriver Path """
    if os == "Linux":
        driver_path = "utils/chromedrivers/chromedriver-linux"
    elif os == "Darwin":
        driver_path = "utils/chromedrivers/chromedriver-mac"
    elif os == "Windows":
        driver_path = "utils/chromedrivers/chromedriver.exe"

    def setUp(self):
        my_path = Path().absolute()
        if my_path.name == "tests":
            driver_location = my_path.parent / self.driver_path
        elif my_path.name == "BuddyForms":
            driver_location = my_path / self.driver_path
        else:
            driver_location = None

        self.driver = webdriver.Chrome(driver_location)
        self.driver.maximize_window()
        self.driver.get(Urls.wordpress_admin_page_apache_auth)
        time.sleep(5)

    def tearDown(self):
        if self.driver is not None:
            self.driver.quit()
