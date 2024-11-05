from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets.check_email_views import CheckEmailView
from .viewsets.logout_views import LogoutView
from .viewsets.user_views import UserViewSet
from .viewsets.reset_password_views import PasswordResetView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')  

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('logout/', LogoutView.as_view(), name='custom_logout'),
    path('check-email/', CheckEmailView.as_view(), name='check_email'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset_email'),
    path('', include(router.urls)),  
]
