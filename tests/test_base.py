from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from django.test import TestCase, tag

DJANGO_URL = 'http://web:8000/'
EXPECTED_TITLE = 'Django'


class InitialConnectionTest(TestCase):

    @tag('base-test')
    def setUp(self):
        self.chrome = webdriver.Remote(
            command_executor='http://selenium_hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.chrome.implicitly_wait(10)
        self.firefox = webdriver.Remote(
            command_executor='http://selenium_hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX
        )

    @tag('base-test')
    def tearDown(self):
        self.chrome.quit()
        self.firefox.quit()

    @tag('base-test')
    def test_chrome_conectivity(self):
        self.chrome.get("https://www.google.com")
        self.assertIn('Google', self.chrome.title)

    @tag('base-test')
    def test_visit_site_with_chrome(self):
        self.chrome.get(DJANGO_URL)
        self.assertIn(EXPECTED_TITLE, self.chrome.title)

    @tag('base-test')
    def test_visit_site_with_firefox(self):
        self.firefox.get(DJANGO_URL)
        self.assertIn(EXPECTED_TITLE, self.firefox.title)
