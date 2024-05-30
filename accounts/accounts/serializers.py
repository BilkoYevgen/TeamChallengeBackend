from rest_framework import serializers
from accounts.models import CustomUser, Role, UserRole


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'phone', 'address', 'is_active', 'is_staff', 'date_joined']


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']


class UserRoleSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    role = RoleSerializer()

    class Meta:
        model = UserRole
        fields = ['id', 'user', 'role']
