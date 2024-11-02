from django.test import TestCase
from login.models import CustomUser

class UserModelTest(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create_user(username="testuser", password="testpass")
        self.assertEqual(user.username, "testuser")
