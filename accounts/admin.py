from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Role
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'created_at', 'updated_at', 'phone', 'address')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'role')
    filter_horizontal = ('role',)
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'role')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'role')}
         ),
    )


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
