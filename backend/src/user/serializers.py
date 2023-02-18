from .models import CustomUser
from rest_framework import serializers
from rest_framework.exceptions import ParseError


class CustomUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        try:
            user = CustomUser.objects.create(
                username=validated_data.get('username'),
                is_staff=validated_data.get('is_staff', False),
                is_active=validated_data.get('is_active', True),
                first_name=validated_data.get('first_name', ''),
                last_name=validated_data.get('last_name', ''),
                email=validated_data.get('email', ''),
            )
            user.set_password(validated_data['password'])
            user.save()

            return user
        except Exception as e:
            raise ParseError(detail=e, code=None)

    class Meta:
        model = CustomUser
        fields = "__all__"