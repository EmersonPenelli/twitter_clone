from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from follows.models import Follow
from follows.serializers import FollowSerializer

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all().order_by('-created_at')
    serializer_class = FollowSerializer
    permission_classes = [AllowAny] 
