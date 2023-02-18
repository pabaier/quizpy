from django.urls import include, path
from .views import CustomUserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', CustomUserViewSet, basename='CustomUserViewSet')

urlpatterns = [
    path('', include(router.urls))
]