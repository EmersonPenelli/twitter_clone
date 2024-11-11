from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from login.models import CustomUser
from rest_framework.exceptions import AuthenticationFailed

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            user = CustomUser.objects.get(email=attrs['email'])
        except CustomUser.DoesNotExist:
            raise AuthenticationFailed('No active account found with the given credentials')

        # Verificando a senha
        if not user.check_password(attrs['password']):
            raise AuthenticationFailed('No active account found with the given credentials')

        data = super().validate(attrs)
        data['user_id'] = user.id
        return data
