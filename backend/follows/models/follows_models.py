from django.db import models
from login.models import CustomUser

class Follow(models.Model):
    follower = models.ForeignKey(CustomUser, related_name="following_set", on_delete=models.CASCADE)
    followed = models.ForeignKey(CustomUser, related_name="followers_set", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'followed')
