from django.contrib import admin

from src.apps.categories.models import Category, SubCategory


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'created_at', 'updated_at')
    list_filter = ('active', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'active', 'created_at', 'updated_at')
    list_filter = ('active', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
