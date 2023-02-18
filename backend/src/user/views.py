from .serializers import CustomUserSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from rest_framework import permissions


class CustomUserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = CustomUserSerializer
