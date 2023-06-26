import uuid

from django.db import models

from src.apps.sections.models.base_model import TimestampMixin


class ContentText(TimestampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.text} - {self.id}'
    

class Button(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    content_text = models.ForeignKey('sections.ContentText', on_delete=models.CASCADE, related_name='buttons')

    def __str__(self):
        return f'{self.text} - {self.id}'
