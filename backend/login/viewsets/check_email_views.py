from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from login.serializers.check_email_serializer import CheckEmailSerializer
from login.models.user_model import CustomUser


class CheckEmailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        serializer = CheckEmailSerializer(data=request.query_params)

        if serializer.is_valid():

            try: 
                email = serializer.validated_data['email']

                user_exists = CustomUser.objects.filter(email=email).exists()

                if user_exists:
                    return Response({"message": "Email exists."}, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Email does not exist."}, status=status.HTTP_404_NOT_FOUND)
            except:
                return Response({"error": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)