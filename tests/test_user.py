
from django.test import TestCase, tag
from django.contrib.auth import get_user_model

User = get_user_model()



class UserModelTest(TestCase):

    def test_user_is_valid_email(self):
        user = User(email = 'a@example.com')
        user.full_clean()
