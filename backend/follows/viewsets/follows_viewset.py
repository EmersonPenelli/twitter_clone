from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from follows.models import Follow
from follows.serializers import FollowSerializer

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all().order_by('-created_at')
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user_to_follow_id = request.data.get('user_id')

        if user_to_follow_id is None:
            return Response({'detail': 'User ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            follow_instance = Follow.objects.filter(follower=request.user, followed_id=user_to_follow_id).first()
            
            if follow_instance:
                follow_instance.delete()
                return Response({'detail': 'Unfollowed successfully.'}, status=status.HTTP_204_NO_CONTENT)
            else:
                follow_instance = Follow.objects.create(
                    follower=request.user,
                    followed_id=user_to_follow_id
                )
                serializer = self.get_serializer(follow_instance)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
