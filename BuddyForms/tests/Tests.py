from selenium.common.exceptions import TimeoutException
from BuddyForms.pages.HomePage import HomePage
from BuddyForms.utils.TestTemplate import TestTemplate
from BuddyForms.pages.LoginPage import LoginPage
from BuddyForms.utils.Urls import Urls


class Tests(TestTemplate):
    def assertUrl(self, url):
        self.assertEqual(url, self.verify_url(), "The URL does not match.")

    def assertText(self, text, method):
        self.assertEqual(text, method, "The text doesn't match.")

    def assertTitle(self, title, method):
        self.assertEqual(title, method, "The title doesn't match.")

    def assertButtonText(self, text, method):
        self.assertEqual(text, method, "The button is not visible.")

    def assertTupleText(self, first, second):
        self.assertTupleEqual(first, second, "The list doesn't match.")

    def verify_url(self):
        try:
            return self.driver.current_url
        except TimeoutException:
            return False

    """ Tests """

    def test_login_process(self):
        login_page = LoginPage(self.driver)
        login_page.login_process()
        home_page = HomePage(self.driver)
        self.assertUrl(Urls.wordpress_admin_page)
        self.assertText("buddyforms-premium.appscidentally.com", home_page.verify_landing_page())
        self.assertTitle("Dashboard", home_page.verify_dashboard_title())
