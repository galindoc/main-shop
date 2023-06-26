import uuid

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from src.apps.sections.models.base_model import TimestampMixin


class Content(TimestampMixin):
    TEXT_ALIGNMENT_CHOICES = (
        ('left', 'Left'),
        ('center', 'Center'),
        ('right', 'Right'),
        ('bottom', 'Bottom'),
        ('top', 'Top'),
        ('over', 'Over'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    section = models.ForeignKey('sections.Section', on_delete=models.CASCADE, related_name='contents')
    text = models.OneToOneField('sections.ContentText', on_delete=models.CASCADE, blank=True, null=True)
    image = models.OneToOneField('sections.ContentImage', on_delete=models.CASCADE, blank=True, null=True)

    width = models.IntegerField(
        default=100,
        validators=[
            MinValueValidator(20), 
            MaxValueValidator(100),  
        ],
    )
    background_color = models.CharField(max_length=255, blank=True, null=True)
    text_alignment = models.CharField(
        max_length=255,
        choices=TEXT_ALIGNMENT_CHOICES,
        default='center',
    )

    def __str__(self):
        return f'{self.text} - {self.id}'