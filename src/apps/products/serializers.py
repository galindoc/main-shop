from rest_framework import serializers
from .models import Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'is_active', 'created_at', 'updated_at']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ['id', 'description', 'price', 'quantity', 'is_active', 'slug', 'created_at', 'updated_at', 'images', 'category', 'subcategory']
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = instance.category.name
        representation['subcategory'] = instance.subcategory.name if instance.subcategory else None
        return representation

    def create(self, validated_data):
        try:
            images_data = self.context.get('view').request.FILES.getlist('images')
            product = Product.objects.create(**validated_data)

            for image_data in images_data[:3]:  # Limiting to 3 images
                ProductImage.objects.create(product=product, image=image_data)

            return product
        except Exception as e:
            raise serializers.ValidationError({'error': str(e)})

    def update(self, instance, validated_data):
        images_data = self.context.get('view').request.FILES.getlist('images')
        instance = super().update(instance, validated_data)

        for image_data in images_data[:3]:  # Limiting to 3 images
            ProductImage.objects.create(product=instance, image=image_data)

        return instance
