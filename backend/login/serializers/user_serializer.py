from rest_framework import serializers
from login.models.user_model import CustomUser
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'email', 'password', 'created_at']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        return make_password(value)
    
    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            name=validated_data['name'],
            bio=validated_data.get('bio', ''),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)

