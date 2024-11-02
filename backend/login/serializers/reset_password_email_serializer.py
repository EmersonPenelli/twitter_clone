from rest_framework import serializers

from login.models.user_model import CustomUser


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            user = CustomUser.objects.get(email=value)
        except:
            raise serializers.ValidationError("Email not found in database!")
        return user