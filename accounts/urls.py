from django.urls import path
from .views import CustomUserViewSet, RoleViewSet, UserActivationView

urlpatterns = [
    path('accounts/users/', CustomUserViewSet.as_view(), name='users'),
    path('accounts/roles/', RoleViewSet.as_view(), name='roles'),
    path('user/verification/<str:uid>/<str:token>', UserActivationView.as_view(), name='activate_user'),
]

