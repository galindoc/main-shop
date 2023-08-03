import uuid

from django.db import models

from src.apps.sections.models.base_model import TimestampMixin
    

class Button(TimestampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(blank=True, null=True, max_length=255)
    link = models.URLField(blank=True, null=True)
    content = models.OneToOneField('sections.SingleImageContent', on_delete=models.CASCADE, related_name='button', blank=True, null=True)

    content_left = models.OneToOneField('sections.DoubleImageContent', on_delete=models.CASCADE, related_name='button_left', blank=True, null=True)
    content_right = models.OneToOneField('sections.DoubleImageContent', on_delete=models.CASCADE, related_name='button_right', blank=True, null=True)

    def __str__(self):
        return f'{self.text} - {self.id}'
