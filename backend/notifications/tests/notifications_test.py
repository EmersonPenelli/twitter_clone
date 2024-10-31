from django.test import TestCase
from notifications.models import Notification
from users.models import CustomUser
from tweets.models import Tweet

class NotificationModelTest(TestCase):
    def test_create_notification(self):
        user = CustomUser.objects.create_user(username="testuser", password="testpass")
        notification = Notification.objects.create(user=user, content="New follower")
        self.assertEqual(notification.content, "New follower")
