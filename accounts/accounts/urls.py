from django.urls import path
from .views import CustomUserViewSet, RoleViewSet, UserRoleViewSet

urlpatterns = [
    path('accounts/users/', CustomUserViewSet.as_view(), name='users'),
    path('accounts/roles/', RoleViewSet.as_view(), name='roles'),
    path('accounts/user-roles/', UserRoleViewSet.as_view(), name='user-roles'),
]

