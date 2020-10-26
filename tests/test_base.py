from django.test import TestCase
from django.urls import resolve

from joboffers.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_homepage(self):
        response = resolve('/')
        self.assertTemplateUsed(response, 'home.html')
