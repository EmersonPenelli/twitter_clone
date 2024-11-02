from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings

from login.serializers.reset_password_email_serializer import PasswordResetSerializer
from login.models.user_model import CustomUser


class CustomPasswordResetView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)

        if serializer.is_valid():
            try:
                email = serializer.validated_data['email']
                user = CustomUser.objects.get(email=email)

                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                reset_url = f"{settings.FRONTEND_METHOD}://{settings.FRONTEND_DOMAIN}:{settings.FRONTEND_PORT}/{settings.FRONTEND_URI}/{uid}/{token}/"

                html_content = render_to_string('login/reset_password_email.html', {
                    'user' : user,
                    'reset_url' : reset_url,
                    'site_name' : settings.SITE_NAME,
                    'uid' : uid,
                    'token' : token
                })
                text_content = strip_tags(html_content)

                email_message = EmailMultiAlternatives(
                    subject = 'Reset Your Password',
                    body = text_content,
                    from_email = settings.EMAIL_HOST_USER,
                    to = [email]
                )

                email_message.attach_alternative(html_content, "text/html")

                email_message.send()

                return Response({"message" : "Password reset email sent!"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response({"error" : f"Error to send email to {email}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)