from rest_framework import viewsets, parsers, status
from rest_framework.response import Response

from src.apps.categories.models import Category, SubCategory
from src.apps.categories.serializers import CategorySerializer, SubCategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
