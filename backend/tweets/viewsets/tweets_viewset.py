from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from tweets.models import Tweet
from tweets.serializers import TweetSerializer

class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all().order_by('-created_at')
    serializer_class = TweetSerializer
    permission_classes = [AllowAny]  

    def get_queryset(self):
        return Tweet.objects.all()

    def update(self, request, *args, **kwargs):
        partial = True
        instance = self.get_object()

        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        if 'likes_count' in request.data:
            current_likes = instance.likes_count
            requested_likes = int(request.data['likes_count']) 
            if requested_likes > current_likes:
                instance.toggle_like(request.user)
                instance.is_liked = True 
            elif requested_likes < current_likes:
                instance.toggle_like(request.user)
                instance.is_liked = False  

        if 'shares_count' in request.data:
            current_shares = instance.shares_count
            requested_shares = int(request.data['shares_count']) 
            if requested_shares > current_shares:
                instance.toggle_share(request.user)
            elif requested_shares < current_shares:
                instance.toggle_share(request.user)

        instance.save()
        
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
