from django.db import models
from login.models import CustomUser
from tweets.models import Tweet

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, related_name="notifications", on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, related_name="tweet_notifications", on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(max_length=255)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
