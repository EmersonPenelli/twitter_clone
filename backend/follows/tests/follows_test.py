from django.test import TestCase
from follows.models import Follow
from users.models import CustomUser

class FollowModelTest(TestCase):
    def test_create_follow(self):
        follower = CustomUser.objects.create_user(username="follower", password="testpass")
        followed = CustomUser.objects.create_user(username="followed", password="testpass")
        follow = Follow.objects.create(follower=follower, followed=followed)
        self.assertEqual(follow.follower, follower)
