from rest_framework import serializers
from tweets.models.tweet_model import Like, Share
from tweets.models import Tweet

class TweetSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name', read_only=True)
    is_liked = serializers.SerializerMethodField()
    is_shared = serializers.SerializerMethodField()
    
    class Meta:
        model = Tweet
        fields = ['id', 'name', 'user', 'content', 'likes_count', 'shares_count', 'created_at', 'is_liked', 'is_shared']

    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Like.objects.filter(user=request.user, tweet=obj).exists()
        return False

    def get_is_shared(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Share.objects.filter(user=request.user, tweet=obj).exists()
        return False
