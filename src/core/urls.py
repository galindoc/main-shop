from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{settings.ENDPOINT_PREFIX}/', include('src.apps.users.urls')),
    path(f'{settings.ENDPOINT_PREFIX}/', include('src.apps.products.urls')),
    path(f'{settings.ENDPOINT_PREFIX}/', include('src.apps.categories.urls')),
    path(f'{settings.ENDPOINT_PREFIX}/', include('src.apps.sections.urls')),
]
