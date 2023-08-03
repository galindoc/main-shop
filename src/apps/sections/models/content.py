import uuid

from django.db import models

from src.apps.sections.models.base_model import TimestampMixin


class SingleImageContent(TimestampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)

    link_wrapper = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='content_images', blank=True, null=True)

    copy = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
    

class DoubleImageContent(TimestampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    name_left = models.CharField(max_length=255, blank=True, null=True)
    link_wrapper_left = models.URLField(blank=True, null=True)
    image_left = models.ImageField(upload_to='content_images')
    image_left = models.ImageField(upload_to='content_images')
    copy_left = models.TextField(blank=True, null=True)

    name_right = models.CharField(max_length=255, blank=True, null=True)
    link_wrapper_right = models.URLField(blank=True, null=True)
    image_right = models.ImageField(upload_to='content_images')
    image_right = models.ImageField(upload_to='content_images')
    copy_right = models.TextField(blank=True, null=True, max_length=510)

    def __str__(self):
        return f'{self.name_left} - {self.name_right}'
