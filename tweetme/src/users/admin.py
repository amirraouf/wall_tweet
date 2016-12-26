from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserCreationForm
from django.contrib import admin
from .models import User
# Register your models here.


class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password', 'first_name', 'last_name')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('user_permissions', 'groups', 'is_superuser', 'slug', 'is_staff', 'last_login', 'is_verified'),
        }),
    )


admin.site.register(User, UserAdmin)
