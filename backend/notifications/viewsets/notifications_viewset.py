from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from notifications.models import Notification
from notifications.serializers import NotificationSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all().order_by('created_at')
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
