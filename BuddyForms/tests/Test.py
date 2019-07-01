from BuddyForms.pages.HomePage import HomePage
from BuddyForms.utils.TestTemplate import TestTemplate
from BuddyForms.pages.LoginPage import LoginPage


class Test(TestTemplate):
    def test_login_process(self):
        login_page = LoginPage(self.driver)
        login_page.login_process()
        home_page = HomePage(self.driver)
        assert home_page.verify_correct_landing_page()
        assert "Howdy, Nery Marin" in home_page.verify_correct_user_access()

