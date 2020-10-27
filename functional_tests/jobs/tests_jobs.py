import os

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from django.test import LiveServerTestCase

from users.models import CustomUser

DJANGO_URL = 'http://web:8000/'

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


class JobOfferTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Remote(
            command_executor='http://selenium_hub:4444/wd/hub',
            desired_capabilities=get_browser_cap(TESTING_BROWSER)
        )

    def tearDown(self):
        self.browser.quit()

    def test_user_posting_job(self):
        # User logs in
        self.fail("Finish User logs in")

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
