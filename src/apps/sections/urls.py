from django.urls import path, include
from rest_framework.routers import DefaultRouter

from src.apps.sections.views import (
    SectionViewSet,
)


router = DefaultRouter()
router.register(r'sections', SectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
