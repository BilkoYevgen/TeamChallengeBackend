from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from accounts.models import CustomUser, Role, UserRole
from .serializers import CustomUserSerializer, RoleSerializer, UserRoleSerializer


class CustomUserViewSet(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class RoleViewSet(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]


class UserRoleViewSet(generics.ListCreateAPIView):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer
