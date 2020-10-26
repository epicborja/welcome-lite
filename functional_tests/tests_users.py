import os

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from django.test import LiveServerTestCase

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


class BaseFunctionalTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Remote(
            command_executor='http://selenium_hub:4444/wd/hub',
            desired_capabilities=get_browser_cap(TESTING_BROWSER)
        )

    def tearDown(self):
        self.browser.quit()

    def test_user_logs(self):
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
        sign_up_button = self.browser.find_element_by_id("sign-up-button")

        self.assertIn('Log In', log_in_button.text)
        self.assertIn('Sign Up', sign_up_button.text)

        # User clicks on log in
        log_in_button.click()
        current_url = self.browser.current_url
        self.assertURLEqual(DJANGO_URL + 'accounts/login/', current_url)

        # As user is not logged, returns to homepage
        home_button = self.browser.find_element_by_id("home-button")
        home_button.click()
        current_url = self.browser.current_url
        self.assertURLEqual(DJANGO_URL, current_url)

        # User signs in
        sign_up_button = self.browser.find_element_by_id("sign-up-button")
        sign_up_button.click()
        current_url = self.browser.current_url
        self.assertURLEqual(DJANGO_URL + 'accounts/signup/', current_url)

        form_email = self.browser.find_element_by_id("id_email")
        form_email.send_keys(TEST_USER_EMAIL)
        form_pass1 = self.browser.find_element_by_id("id_password1")
        form_pass1.send_keys(TEST_USER_PASS)
        form_pass2 = self.browser.find_element_by_id("id_password2")
        form_pass2.send_keys(TEST_USER_PASS)
        signup_send = self.browser.find_element_by_id("id_signup")
        signup_send.click()

        # Now user is back on homepage
        current_url = self.browser.current_url
        self.assertURLEqual(DJANGO_URL, current_url)

