from rest_framework import serializers
from .models import CustomUser, Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']


class CustomUserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(source='role', many=True)
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = (
            'email', 'password', 'password2', 'first_name', 'last_name', 'phone', 'address', 'role', 'is_superuser',
            'is_active', 'is_staff', 'created_at', 'updated_at', 'roles'
        )
        extra_kwargs = {
            'is_active': {'read_only': True},
            'is_staff': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
