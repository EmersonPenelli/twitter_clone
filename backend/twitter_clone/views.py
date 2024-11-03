from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.reverse import reverse

@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'follows': reverse('follow-list', request=request, format=format),
        'tweets': reverse('tweet-list', request=request, format=format),
        'notifications': reverse('notification-list', request=request, format=format),
    })
