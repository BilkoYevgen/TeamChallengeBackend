from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser, Role
from .serializers import CustomUserSerializer, RoleSerializer


class CustomUserViewSet(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class RoleViewSet(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]
