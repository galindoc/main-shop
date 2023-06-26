import uuid

from django.db import models

from src.apps.sections.models.base_model import TimestampMixin


class ContentImage(TimestampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='content_images')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.image} - {self.id}'
    