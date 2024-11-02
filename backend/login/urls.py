from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets.check_email_views import CheckEmailView
from .viewsets.logout_views import LogoutView
from .viewsets.user_views import CustomTokenObtainPairView, UserViewSet
from .viewsets.reset_password_email_views import CustomPasswordResetView
from .viewsets.reset_password_confirm_views import PasswordChangeConfirmView

# Crie um router e registre o UserViewSet
router = DefaultRouter()
router.register(r'register', UserViewSet, basename='user')  

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('login/', CustomTokenObtainPairView.as_view(), name='custom_login'),
    path('logout/', LogoutView.as_view(), name='custom_logout'),
    path('check-email/', CheckEmailView.as_view(), name='check_email'),
    path('password/email/', CustomPasswordResetView.as_view(), name='password_reset_email'),
    path('password/confirm/', PasswordChangeConfirmView.as_view(), name='password_reset_confirm'),
    path('', include(router.urls)),  
]
