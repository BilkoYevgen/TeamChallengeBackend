from django.urls import path
from .views import CustomUserViewSet, RoleViewSet

urlpatterns = [
    path('accounts/users/', CustomUserViewSet.as_view(), name='users'),
    path('accounts/roles/', RoleViewSet.as_view(), name='roles'),
]

