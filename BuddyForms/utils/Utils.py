from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Utils(object):
    def __init__(self, driver):
        self._driver = driver

    def wait_visibility_element_displayed(self, locator):
        try:
            wait = WebDriverWait(self._driver, 10)
            return wait.until(ec.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return "The element is not present"

    def wait_visibility_all_elements_displayed(self, locator):
        try:
            wait = WebDriverWait(self._driver, 10)
            elementList = wait.until(ec.visibility_of_all_elements_located(locator))
            return elementList
        except TimeoutException:
            return "The elements are not present"

    def wait_clickable_element_and_click(self, locator):
        try:
            wait = WebDriverWait(self._driver, 10)
            wait.until(ec.element_to_be_clickable(locator)).click()
        except TimeoutException:
            return "The element is not present"
        return True

    def wait_element_displayed_text(self, locator):
        try:
            wait = WebDriverWait(self._driver, 10)
            return wait.until(ec.visibility_of_element_located(locator)).text
        except TimeoutException:
            return "The element is not present"

    def wait_visibility_element_send_keys(self, locator, keys):
        try:
            wait = WebDriverWait(self._driver, 10)
            wait.until(ec.visibility_of_element_located(locator)).send_keys(keys)
        except TimeoutException:
            return "The element is not present"
        return True

    def validate_current_url(self):
        try:
            return self._driver.current_url
        except TimeoutException:
            return False

    def get_attribute_placeholder(self, locator):
        try:
            wait = WebDriverWait(self._driver, 10)
            element = wait.until(ec.visibility_of_element_located(locator))
            return element.get_attribute("placeholder")
        except TimeoutException:
            return "The placeholder is not present"

    def get_attribute_value(self, locator):
        try:
            wait = WebDriverWait(self._driver, 10)
            element = wait.until(ec.visibility_of_element_located(locator))
            return element.get_attribute("value")
        except TimeoutException:
            return False
