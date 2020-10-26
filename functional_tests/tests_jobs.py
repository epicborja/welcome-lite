import os

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from django.test import LiveServerTestCase

from users.models import CustomUser

DJANGO_URL = 'http://web:8000/'

TESTING_BROWSER = os.environ.get('TESTING_BROWSER')

TEST_USER_EMAIL = 'testuser@example.com'
TEST_USER_PASS = 'themostUnsecurepass123'


def get_browser_cap(desired_browser):
    """Whether to use firefox or chrome for testing ("""
    if desired_browser == 'Firefox':
        caps = DesiredCapabilities.FIREFOX

    elif desired_browser == 'Chrome':
        caps = DesiredCapabilities.CHROME

    else:
        caps = DesiredCapabilities.FIREFOX  # Default
    return caps


class JobOfferTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Remote(
            command_executor='http://selenium_hub:4444/wd/hub',
            desired_capabilities=get_browser_cap(TESTING_BROWSER)
        )

    def tearDown(self):
        self.browser.quit()

    def test_login(self):
        # User goes to webpage
        self.browser.get(DJANGO_URL)
        self.assertIn('WelcomeLite Home', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Home', header_text)

        # User is not logged in
        is_logged_text = self.browser.find_elements_by_class_name(
            "is-logged-text")[0].text
        self.assertIn('not logged', is_logged_text)

        log_in_button = self.browser.find_element_by_id("log-in-button")
        self.assertIn('Log In', log_in_button.text)

        # User clicks on log in
        log_in_button.click()
        current_url = self.browser.current_url
        self.assertURLEqual(DJANGO_URL + 'accounts/login/', current_url)

        # User logs in
        form_email = self.browser.find_element_by_id("id_login")
        form_email.send_keys(TEST_USER_EMAIL)
        form_pass = self.browser.find_element_by_id("id_password")
        form_pass.send_keys(TEST_USER_PASS)

        login = self.browser.find_element_by_id("login_button")
        login.click()

        # Now user is back on homepage
        current_url = self.browser.current_url
        self.assertURLEqual(DJANGO_URL, current_url)

    def test_user_posting_job(self):
        # User logs in
        self.fail("User logs in")

        # User posts a new job
        self.fail("Finish user post new job offer")

        # User can see their posted jobs
        self.fail("Finish user list job offers")

        # User can edit one single job
        self.fail("Finish user edits job offer")

        # User deletes job offer
        self.fail("Finish user deletes job offer")

        # User deletes job offer
        self.fail("Finish user deletes job offer")

        # User deletes logs out
        self.fail("Finish user logs out")
