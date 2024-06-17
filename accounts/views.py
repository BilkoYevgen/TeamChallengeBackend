from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
import os
from .models import CustomUser, Role
from .serializers import CustomUserSerializer, RoleSerializer
from rest_framework.views import APIView
from django.shortcuts import redirect


class CustomUserViewSet(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class RoleViewSet(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]


class UserActivationView(APIView):
    def get(self, request, uid, token):
        return redirect(f"{os.environ.get('FRONTEND_URL')}/user/verification/{uid}/{token}")
