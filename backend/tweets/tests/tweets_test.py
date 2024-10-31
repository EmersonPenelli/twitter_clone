from django.test import TestCase
from tweets.models import Tweet
from users.models import CustomUser

class TweetModelTest(TestCase):
    def test_create_tweet(self):
        user = CustomUser.objects.create_user(username="testuser", password="testpass")
        tweet = Tweet.objects.create(user=user, content="Hello World")
        self.assertEqual(tweet.content, "Hello World")
