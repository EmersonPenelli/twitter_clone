from rest_framework import serializers
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

from login.models.user_model import CustomUser


class PasswordResetConfirmSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField()

    def validate(self, data):
        try:
            uid = urlsafe_base64_decode(data['uid']).decode()
            user = CustomUser.objects.get(pk=uid)
        except (CustomUser.DoesNotExist, ValueError, TypeError, OverflowError):
            raise serializers.ValidationError('Invalid UID or user not found.')
        
        if not default_token_generator.check_token(user, data['token']):
            raise serializers.ValidationError('Invalid or expired token.')
        
        return {'user' : user, 'new_password' : data['new_password']}
    
    def save(self):
        user = self.validated_data['user']
        new_password = self.validated_data['new_password']
        user.set_password(new_password)
        user.save()