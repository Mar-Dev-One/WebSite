from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "username", "role", "is_active", "is_staff", "is_superuser", "is_verified")
    list_filter = ("role", "is_active", "is_staff", "is_superuser", "is_verified")
    search_fields = ("email", "username", "phone_number")
    ordering = ("-date_joined",)

    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        ("Personal info", {"fields": ("phone_number", "date_of_birth", "bio", "profile_picture")}),
        ("Permissions", {"fields": ("role", "is_active", "is_staff", "is_superuser", "is_verified", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "password1", "password2", "role", "is_active", "is_staff", "is_superuser")}
        ),
    )
