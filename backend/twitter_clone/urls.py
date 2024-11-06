from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from login.viewsets.token_views import CustomTokenObtainPairView
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
    path("api/v1/", include(router.urls)),  
    path("api/v1/login/", include("login.urls")),
    path('api/v1/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
