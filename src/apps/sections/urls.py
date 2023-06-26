from django.urls import path, include
from rest_framework.routers import DefaultRouter

from src.apps.sections.views import (
    ContentTextViewSet, 
    ButtonViewSet, 
    ContentImageViewSet,
    ContentViewSet,
    SectionViewSet,
)


router = DefaultRouter()
router.register(r'content-texts', ContentTextViewSet)
router.register(r'buttons', ButtonViewSet)
router.register(r'content-images', ContentImageViewSet)
router.register(r'contents', ContentViewSet)
router.register(r'sections', SectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('sections/<uuid:pk>/add-content/', SectionViewSet.as_view({'post': 'add_content'})),
    path('sections/<uuid:pk>/remove-content/', SectionViewSet.as_view({'post': 'remove_content'})),
]
