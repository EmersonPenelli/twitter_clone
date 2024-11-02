from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from login.viewsets import UserViewSet
from follows.viewsets import FollowViewSet
from tweets.viewsets import TweetViewSet
from notifications.viewsets import NotificationViewSet

# Definindo o router e registrando as views
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'follows', FollowViewSet)
router.register(r'tweets', TweetViewSet)
router.register(r'notifications', NotificationViewSet)

# Configuração das URLs
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),  
    path("api/auth/", include("login.urls")), 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
