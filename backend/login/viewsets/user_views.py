from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from login.models.user_model import CustomUser
from follows.models import Follow
from login.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by("-created_at")
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        current_user = request.user
        if current_user.is_authenticated:
            queryset = queryset.exclude(id=current_user.id)

        users_data = []
        for user in queryset:
            serializer = self.get_serializer(user)
            user_data = serializer.data

            user_data['is_following'] = (
                Follow.objects.filter(follower=current_user, followed=user).exists()
                if current_user.is_authenticated
                else False
            )
            users_data.append(user_data)

        return Response(users_data)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()

        password = data.get('password')
        password_confirmation = data.get('password_confirmation')

        if password != password_confirmation:
            return Response(
                {"Error": "Passwords do not match."},
                status=status.HTTP_400_BAD_REQUEST
            )
    
        data.pop('password_confirmation', None)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = True
        user = self.get_object()

        if not request.user.is_authenticated:
            return Response({'detail': 'Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        if user != request.user:
            return Response({'detail': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

        user.is_premium = not user.is_premium
        user.save()

        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
