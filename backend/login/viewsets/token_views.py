from rest_framework_simplejwt.views import TokenObtainPairView
from login.serializers.token_serializer import CustomTokenObtainPairSerializer
from rest_framework.permissions import AllowAny

class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = CustomTokenObtainPairSerializer