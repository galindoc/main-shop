from rest_framework import serializers

from src.apps.categories.models import Category, SubCategory
from src.apps.products.serializers import ProductSerializer


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get('include_products', False):
            representation['products'] = ProductSerializer(instance.products.all(), many=True).data
        return representation


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['subcategories'] = SubCategorySerializer(instance.subcategories.all(), many=True).data
        if self.context.get('include_products', False):
            representation['products'] = ProductSerializer(instance.products.all(), many=True).data
        return representation
