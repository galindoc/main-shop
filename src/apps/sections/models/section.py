import uuid

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from src.apps.sections.models.base_model import TimestampMixin


class Section(TimestampMixin):
    SECTION_TYPE_CHOICES = (
        ('single_image', 'Single Image'),
        ('double_image', 'Double Image'),
        ('products_list', 'Products List'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    section_type = models.CharField(max_length=255, choices=SECTION_TYPE_CHOICES)
    active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    double_image_content = models.OneToOneField('sections.DoubleImageContent', on_delete=models.CASCADE, related_name='section', blank=True, null=True)
    single_image_content = models.OneToOneField('sections.SingleImageContent', on_delete=models.CASCADE, related_name='section', blank=True, null=True)

    class Meta:
        ordering = ('sort_order',)
    
    def __str__(self):
        return f'{self.sort_order} - {self.name}'
    