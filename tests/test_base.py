from django.test import TestCase
from django.urls import resolve, reverse

from pages.views import HomePageView


class HomePageTest(TestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_root_url_resolves_homepage(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Welcome')

    def test_homepage_does_not_contains_Django(self):
        self.assertNotContains(self.response, 'Django')

    def test_homepage_resolves_view(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )
