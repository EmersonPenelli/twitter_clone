from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from login.serializers.logout_serializer import LogoutSerializer

class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LogoutSerializer(data=request.data)

        if serializer.is_valid():
            try:
                token = serializer.data['refresh']
                current_token = OutstandingToken.objects.filter(token=token).values('id')
                
                if not current_token.exists():
                    return Response({'detail':'Token not found!'}, status=status.HTTP_404_NOT_FOUND)
                
                BlacklistedToken.objects.create(
                    token_id = current_token[0]['id']
                )

                return Response({'detail':'Logout successfully!'}, status=status.HTTP_204_NO_CONTENT)
            except:
                return Response({'detail':'Your token has been closed!'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)