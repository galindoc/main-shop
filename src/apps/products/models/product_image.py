import uuid

from django.db import models


class ProductImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(
        'products.Product', 
        on_delete=models.CASCADE,
        related_name='images',
    )
    image = models.ImageField(upload_to='product_images', blank=False, null=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)