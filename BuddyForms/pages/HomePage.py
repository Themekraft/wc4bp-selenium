from BuddyForms.utils.BasePage import BasePage


class HomePage(BasePage):

    DASHBOARD = "//h1[contains(.,\"Dashboard\")]"
    GREETINGS_USER = "#wp-admin-bar-my-account > a"

    def verify_correct_landing_page(self):
        return self._driver.find_element_by_xpath(HomePage.DASHBOARD).is_displayed()

    def verify_correct_user_access(self):
        return self._driver.find_element_by_css_selector(HomePage.GREETINGS_USER).text
