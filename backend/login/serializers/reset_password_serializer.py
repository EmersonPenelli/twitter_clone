# serializers.py
from rest_framework import serializers
from login.models.user_model import CustomUser

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    new_password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError("As senhas não coincidem.")
        
        user = CustomUser.objects.filter(email=attrs.get('email')).first()
        if user and user.check_password(attrs.get('new_password')):
            raise serializers.ValidationError("The new password cannot be the same as the old password.")
        
        return attrs
