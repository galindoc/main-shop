from django.contrib import admin

from src.apps.products.models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ('description', 'price', 'quantity', 'is_active', 'created_at', 'updated_at', 'slug', 'category', 'subcategory')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('description', 'price', 'quantity', 'slug')
    ordering = ('description',)
    inlines = [ProductImageInline]


admin.site.register(Product, ProductAdmin)
