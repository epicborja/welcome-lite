from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from django.test import TestCase, tag

DJANGO_URL = 'http://web:8000/'
EXPECTED_TITLE = 'Django'



