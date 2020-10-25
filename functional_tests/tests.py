import os

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time
import unittest

DJANGO_URL = 'http://web:8000/'
EXPECTED_TITLE = 'Django'

TESTING_BROWSER = os.environ.get('TESTING_BROWSER')


def get_browser_cap(desired_browser):
    """Whether to use firefox or chrome for testing ("""
    if desired_browser == 'Firefox':
        caps = DesiredCapabilities.FIREFOX

    elif desired_browser == 'Chrome':
        caps = DesiredCapabilities.CHROME

    else:
        caps = DesiredCapabilities.FIREFOX  # Default
    return caps


class InitialConnectionTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Remote(
            command_executor='http://selenium_hub:4444/wd/hub',
            desired_capabilities=get_browser_cap(TESTING_BROWSER)
        )

    def tearDown(self):
        self.browser.quit()

    def test_user_posting_a_job(self):
        # User goes to webpage
        self.browser.get(DJANGO_URL)
        self.assertIn(EXPECTED_TITLE, self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(EXPECTED_TITLE, header_text)

        # User is not logged in
        is_logged_text = self.browser.find_elements_by_id("is-logged-text").text
        self.assertIn('not logged', is_logged_text)

        log_in_button = self.browser.find_element_by_id("log-in-button")
        sign_in_button = self.browser.find_element_by_id("sign-in-button")

        self.assertIn('Sign in', sign_in_button.get_attribute('placeholder'))
        self.assertIn('Log in', log_in_button.get_attribute('placeholder'))

        # User signs in
        self.fail("Finish user signs in")

        # User logs in
        self.fail("Finish user logs in")

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
