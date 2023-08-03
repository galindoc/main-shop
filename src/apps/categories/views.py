from rest_framework import viewsets, parsers, status
from rest_framework.response import Response

from src.apps.categories.models import Category, SubCategory
from src.apps.categories.serializers import CategorySerializer, SubCategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CategorySerializer(instance, context={'include_products': True})
        return Response(serializer.data)


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SubCategorySerializer(instance, context={'include_products': True})
        return Response(serializer.data)
