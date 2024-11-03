from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from tweets.models import Tweet
from tweets.serializers import TweetSerializer

class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all().order_by('-created_at')
    serializer_class = TweetSerializer
    permission_classes = [AllowAny]
