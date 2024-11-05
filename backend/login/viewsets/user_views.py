from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from login.models.user_model import CustomUser
from follows.models import Follow
from login.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by("-created_at")
    serializer_class = UserSerializer
    permission_classes = [AllowAny] 

    def list(self, request, *args, **kwargs):
        current_user = request.user
        queryset = self.get_queryset().exclude(id=current_user.id) 

        users_data = []
        for user in queryset:
            serializer = self.get_serializer(user)
            user_data = serializer.data
            user_data['is_following'] = Follow.objects.filter(follower=current_user, followed=user).exists()
            users_data.append(user_data)

        return Response(users_data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
