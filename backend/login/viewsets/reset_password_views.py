# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from login.models import CustomUser
from rest_framework.permissions import AllowAny
from login.serializers.reset_password_serializer import PasswordResetSerializer  # Importando o serializer

class PasswordResetView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            new_password = serializer.validated_data['new_password']

            try:
                user = CustomUser.objects.get(email=email)
                user.set_password(new_password)  
                user.save()  

                return Response({"success": True, "message": "Senha redefinida com sucesso."}, status=status.HTTP_200_OK)
            except CustomUser.DoesNotExist:
                return Response({"success": False, "message": "E-mail não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
