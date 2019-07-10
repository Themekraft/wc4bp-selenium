from selenium.webdriver.common.by import By

from BuddyForms.utils.Utils import Utils


class HomePage(Utils):
    dashboard_title = By.CSS_SELECTOR, "#wpbody-content > div.wrap > h1"
    wordpress_bar_site = By.CSS_SELECTOR, "#wp-admin-bar-site-name > a"

    def verify_dashboard_title(self):
        return Utils.wait_element_displayed_text(self, self.dashboard_title)

    def verify_landing_page(self):
        return Utils.wait_element_displayed_text(self, self.wordpress_bar_site)
