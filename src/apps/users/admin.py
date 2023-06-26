from django.contrib import admin

from src.apps.users.models import UserAccount


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'username', 'is_staff', 'is_verified', 'created_at', 'last_login', 'updated_at', 'slug')
    list_filter = ('is_staff', 'is_verified', 'created_at', 'last_login', 'updated_at')
    search_fields = ('email', 'name', 'username')
    ordering = ('email',)

admin.site.register(UserAccount, CustomUserAdmin)
