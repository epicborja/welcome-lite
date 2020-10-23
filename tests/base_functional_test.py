import unittest

from selenium import webdriver

from utils.django import get_host, get_port

host = get_host()
django_port = get_port()


# Test for Django running
class InitialConnectionTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_open_homepage(self):
        self.browser.get(f'http://{host}:{django_port}')
        self.assertIn('Django', self.browser.title)

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()
