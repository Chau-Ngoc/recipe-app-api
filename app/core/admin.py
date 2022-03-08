from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    ordering = ["id"]
    search_fields = ["email", "first_name", "last_name"]
    list_display = ["email", "first_name", "last_name"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Your Full Name", {"fields": [("first_name", "last_name")]}),
        ("Groups", {"fields": ["groups"]}),
        (
            "Permissions",
            {
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                ],
                "classes": ["collapse"],
            },
        ),
        (None, {"fields": ["last_login"]}),
    ]
    add_fieldsets = [(None, {"fields": ["email", "password1", "password2"]})]


admin.site.register(User, CustomUserAdmin)
