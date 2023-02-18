from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('games/', include('game.urls')),
    path('questions/', include('question.urls')),
    path('users/', include('user.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/jwt-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/jwt-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/jwt-verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('play/', include('play.urls')),
]
