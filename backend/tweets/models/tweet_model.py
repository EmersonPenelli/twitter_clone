from django.conf import settings
from django.db import models
from login.models.user_model import CustomUser

class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="tweets_user_id")
    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="tweets_user_name", null=True)
    content = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

    likes_count = models.PositiveIntegerField(default=0)       
    shares_count = models.PositiveIntegerField(default=0)        

    def __str__(self):
        return self.content
    
    def toggle_like(self, user):
        like, created = Like.objects.get_or_create(user=user, tweet=self)
        if created:
            self.likes_count += 1
        else:
            like.delete()
            self.likes_count -= 1
        self.save()

    def toggle_share(self, user):
        share, created = Share.objects.get_or_create(user=user, tweet=self)
        if not created:
            share.delete()
            if self.shares_count > 0:  
                self.shares_count -= 1
        else:
            self.shares_count += 1
        self.save()
    
class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ('user', 'tweet')  

    def __str__(self):
        return f"{self.user} likes {self.tweet}"

class Share(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='shares')

    class Meta:
        unique_together = ('user', 'tweet') 

    def __str__(self):
        return f"{self.user} shares {self.tweet}"