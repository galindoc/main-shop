from django.contrib import admin

from src.apps.categories.models import Category, SubCategory


class SubCategoryInline(admin.TabularInline):
    readonly_fields = ('id',)
    model = SubCategory
    exclude = ('slug',)
    extra = 0


class SubCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('name', 'active', 'created_at', 'updated_at')
    list_filter = ('active', 'created_at', 'updated_at')
    search_fields = ('name',)
    exclude = ('slug',)
    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('name', 'active', 'created_at', 'updated_at')
    list_filter = ('active', 'created_at', 'updated_at')
    search_fields = ('name',)
    exclude = ('slug',)
    ordering = ('name',)
    inlines = [SubCategoryInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
