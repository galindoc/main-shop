from django.urls import path, include
from rest_framework.routers import DefaultRouter

from src.apps.categories.views import CategoryViewSet, SubCategoryViewSet

router = DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
