from django.contrib import admin

from src.apps.products.models import Product, ProductImage, CustomProductList


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ('description', 'price', 'quantity', 'is_active',)
    list_filter = ('is_active', 'created_at', 'updated_at',)
    search_fields = ('description', 'price', 'quantity',)
    exclude = ('slug',)
    ordering = ('updated_at',)
    inlines = [ProductImageInline]


class CustomProductListAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)
    list_filter = ('created_at', 'updated_at',)
    search_fields = ('name',)
    ordering = ('updated_at',)


admin.site.register(Product, ProductAdmin)
admin.site.register(CustomProductList, CustomProductListAdmin)
