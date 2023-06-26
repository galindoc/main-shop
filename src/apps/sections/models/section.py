import uuid

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from src.apps.sections.models.base_model import TimestampMixin


class Section(TimestampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    active = models.BooleanField(default=True)
    order = models.IntegerField(unique=True, validators=[MinValueValidator(1), MaxValueValidator(10)])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f'{self.order} - {self.id}'
    