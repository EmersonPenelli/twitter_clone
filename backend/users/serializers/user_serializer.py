from rest_framework import serializers
from users.models.user_models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'bio', 'profile_image', 'followers', 'following']
